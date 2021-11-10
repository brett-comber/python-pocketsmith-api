# coding: utf-8

"""
    PocketSmith

    The public PocketSmith API  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: api@pocketsmith.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pocketsmith.configuration import Configuration


class Form(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'approximate_expiry_at': 'datetime',
        'encryption': 'str',
        'public_key': 'str',
        'rows': 'list[FormRows]'
    }

    attribute_map = {
        'approximate_expiry_at': 'approximate_expiry_at',
        'encryption': 'encryption',
        'public_key': 'public_key',
        'rows': 'rows'
    }

    def __init__(self, approximate_expiry_at=None, encryption=None, public_key=None, rows=None, local_vars_configuration=None):  # noqa: E501
        """Form - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._approximate_expiry_at = None
        self._encryption = None
        self._public_key = None
        self._rows = None
        self.discriminator = None

        self.approximate_expiry_at = approximate_expiry_at
        if encryption is not None:
            self.encryption = encryption
        if public_key is not None:
            self.public_key = public_key
        if rows is not None:
            self.rows = rows

    @property
    def approximate_expiry_at(self):
        """Gets the approximate_expiry_at of this Form.  # noqa: E501

        Estimated time when the form will no longer accept submissions  # noqa: E501

        :return: The approximate_expiry_at of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._approximate_expiry_at

    @approximate_expiry_at.setter
    def approximate_expiry_at(self, approximate_expiry_at):
        """Sets the approximate_expiry_at of this Form.

        Estimated time when the form will no longer accept submissions  # noqa: E501

        :param approximate_expiry_at: The approximate_expiry_at of this Form.  # noqa: E501
        :type: datetime
        """

        self._approximate_expiry_at = approximate_expiry_at

    @property
    def encryption(self):
        """Gets the encryption of this Form.  # noqa: E501

        Type of encryption employed by the form  # noqa: E501

        :return: The encryption of this Form.  # noqa: E501
        :rtype: str
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this Form.

        Type of encryption employed by the form  # noqa: E501

        :param encryption: The encryption of this Form.  # noqa: E501
        :type: str
        """
        allowed_values = ["pki"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and encryption not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `encryption` ({0}), must be one of {1}"  # noqa: E501
                .format(encryption, allowed_values)
            )

        self._encryption = encryption

    @property
    def public_key(self):
        """Gets the public_key of this Form.  # noqa: E501

        RSA public key in PKCS#8 PEM format with which to encrypt values of encrypted fields with  # noqa: E501

        :return: The public_key of this Form.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Form.

        RSA public key in PKCS#8 PEM format with which to encrypt values of encrypted fields with  # noqa: E501

        :param public_key: The public_key of this Form.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def rows(self):
        """Gets the rows of this Form.  # noqa: E501

        Rows of form fields to display  # noqa: E501

        :return: The rows of this Form.  # noqa: E501
        :rtype: list[FormRows]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Form.

        Rows of form fields to display  # noqa: E501

        :param rows: The rows of this Form.  # noqa: E501
        :type: list[FormRows]
        """

        self._rows = rows

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Form):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Form):
            return True

        return self.to_dict() != other.to_dict()
