# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MmeCapabilities(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, non_ip_supported=False):  # noqa: E501
        """MmeCapabilities - a model defined in Swagger

        :param non_ip_supported: The non_ip_supported of this MmeCapabilities.  # noqa: E501
        :type non_ip_supported: bool
        """
        self.swagger_types = {
            'non_ip_supported': bool
        }

        self.attribute_map = {
            'non_ip_supported': 'nonIpSupported'
        }
        self._non_ip_supported = non_ip_supported

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MmeCapabilities of this MmeCapabilities.  # noqa: E501
        :rtype: MmeCapabilities
        """
        return util.deserialize_model(dikt, cls)

    @property
    def non_ip_supported(self):
        """Gets the non_ip_supported of this MmeCapabilities.


        :return: The non_ip_supported of this MmeCapabilities.
        :rtype: bool
        """
        return self._non_ip_supported

    @non_ip_supported.setter
    def non_ip_supported(self, non_ip_supported):
        """Sets the non_ip_supported of this MmeCapabilities.


        :param non_ip_supported: The non_ip_supported of this MmeCapabilities.
        :type non_ip_supported: bool
        """

        self._non_ip_supported = non_ip_supported