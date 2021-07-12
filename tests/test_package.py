from datetime import timedelta


def it_imports():
    try:
        import pocketsmith
    except Exception as e:
        raise AssertionError(f'Encountered error importing library: {e}')


def it_makes_request():
    import pocketsmith
    client = pocketsmith.PocketsmithClient('dummy-api-key')

    try:
        client.users.get_me()
    except pocketsmith.ApiException:
        pass
    except Exception as e:
        raise AssertionError(f'Encountered error making request: {e}')

def it_gets_data():
    """Make requests and verify returned data
    
    This test shall verify data is returned successfully from specific end points
    which have failed in previous versions. A free test account can be used to run
    this test against. You can make one with these steps.

    1. Create a new Basic (free) account
    2. Once you have created the account and you are on the Let's get started! page, 
       instead of following the checklist, you can click See More > at the bottom of the page.
    3. From here, you want to select DEMO MODE which will then populate your account with the sample data  
    4. Go to Settings->Categories. If there is a warning that the number of categories exceeds the limit
       of a free account, delete some categories, otherwise the API may reject the requests.
    """
    import pocketsmith
    import itertools
    from datetime import datetime, timedelta

    demo_api_key="212411286192def00ef2fb1c72e3175de32ea8d4431f18bdb3d80dc4c82ed34c2576817b9761ed9e02c96fb5d1b19f57ecdc3b3eddc41321d7370475522d9fce"
    client = pocketsmith.PocketsmithClient(demo_api_key)  
    my_id = client.users.get_me().id
    
    top_level_cats = client.categories.list_categories(my_id)
    assert type(top_level_cats[0]) == type(pocketsmith.Category()), "list_categories must return a list of Category types"
    top_cat_ids = [cat.id for cat in top_level_cats]
    
    accounts = client.accounts.list_accounts(my_id)
    assert type(accounts[0]) == type(pocketsmith.Account()), "list_accounts must return a list of Account types"

    scenario_ids = [scenario.id for scenario in list(itertools.chain(*[account.scenarios for account in accounts]))]
        
    gta = client.budgeting.get_trend_analysis(my_id, "months", "1", str(datetime.today() - timedelta(days=4))[0:10], str(datetime.today() - timedelta(days=0))[0:10], str(top_cat_ids)[1:-1], str(scenario_ids)[1:-1])    
    assert type(pocketsmith.models.BudgetAnalysisPackage()) == type(gta), "trend_analysis must return a BudgetAnalyisPackage type"
    assert type(gta.expense.periods[0].actual_amount) == type(float()), "Failed to retreive actual_amount from BudgetAnalysisPackage"

