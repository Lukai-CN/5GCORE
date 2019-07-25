# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ambr import Ambr  # noqa: F401,E501
from swagger_server.models.cause import Cause  # noqa: F401,E501
from swagger_server.models.duration_sec import DurationSec  # noqa: F401,E501
from swagger_server.models.ebi_arp_mapping import EbiArpMapping  # noqa: F401,E501
from swagger_server.models.eps_bearer_id import EpsBearerId  # noqa: F401,E501
from swagger_server.models.eps_bearer_info import EpsBearerInfo  # noqa: F401,E501
from swagger_server.models.procedure_transaction_id import ProcedureTransactionId  # noqa: F401,E501
from swagger_server.models.qos_flow_add_modify_request_item import QosFlowAddModifyRequestItem  # noqa: F401,E501
from swagger_server.models.qos_flow_release_request_item import QosFlowReleaseRequestItem  # noqa: F401,E501
from swagger_server.models.ref_to_binary_data import RefToBinaryData  # noqa: F401,E501
from swagger_server.models.request_indication import RequestIndication  # noqa: F401,E501
from swagger_server.models.supported_features import SupportedFeatures  # noqa: F401,E501
from swagger_server.models.uri import Uri  # noqa: F401,E501
from swagger_server import util


class VsmfUpdateData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, request_indication=None, session_ambr=None, qos_flows_add_mod_request_list=None, qos_flows_rel_request_list=None, eps_bearer_info=None, assign_ebi_list=None, revoke_ebi_list=None, modified_ebi_list=None, pti=None, n1_sm_info_to_ue=None, always_on_granted=False, hsmf_pdu_session_uri=None, supported_features=None, cause=None, n1sm_cause=None, back_off_timer=None):  # noqa: E501
        """VsmfUpdateData - a model defined in Swagger

        :param request_indication: The request_indication of this VsmfUpdateData.  # noqa: E501
        :type request_indication: RequestIndication
        :param session_ambr: The session_ambr of this VsmfUpdateData.  # noqa: E501
        :type session_ambr: Ambr
        :param qos_flows_add_mod_request_list: The qos_flows_add_mod_request_list of this VsmfUpdateData.  # noqa: E501
        :type qos_flows_add_mod_request_list: List[QosFlowAddModifyRequestItem]
        :param qos_flows_rel_request_list: The qos_flows_rel_request_list of this VsmfUpdateData.  # noqa: E501
        :type qos_flows_rel_request_list: List[QosFlowReleaseRequestItem]
        :param eps_bearer_info: The eps_bearer_info of this VsmfUpdateData.  # noqa: E501
        :type eps_bearer_info: List[EpsBearerInfo]
        :param assign_ebi_list: The assign_ebi_list of this VsmfUpdateData.  # noqa: E501
        :type assign_ebi_list: List[EpsBearerId]
        :param revoke_ebi_list: The revoke_ebi_list of this VsmfUpdateData.  # noqa: E501
        :type revoke_ebi_list: List[EpsBearerId]
        :param modified_ebi_list: The modified_ebi_list of this VsmfUpdateData.  # noqa: E501
        :type modified_ebi_list: List[EbiArpMapping]
        :param pti: The pti of this VsmfUpdateData.  # noqa: E501
        :type pti: ProcedureTransactionId
        :param n1_sm_info_to_ue: The n1_sm_info_to_ue of this VsmfUpdateData.  # noqa: E501
        :type n1_sm_info_to_ue: RefToBinaryData
        :param always_on_granted: The always_on_granted of this VsmfUpdateData.  # noqa: E501
        :type always_on_granted: bool
        :param hsmf_pdu_session_uri: The hsmf_pdu_session_uri of this VsmfUpdateData.  # noqa: E501
        :type hsmf_pdu_session_uri: Uri
        :param supported_features: The supported_features of this VsmfUpdateData.  # noqa: E501
        :type supported_features: SupportedFeatures
        :param cause: The cause of this VsmfUpdateData.  # noqa: E501
        :type cause: Cause
        :param n1sm_cause: The n1sm_cause of this VsmfUpdateData.  # noqa: E501
        :type n1sm_cause: str
        :param back_off_timer: The back_off_timer of this VsmfUpdateData.  # noqa: E501
        :type back_off_timer: DurationSec
        """
        self.swagger_types = {
            'request_indication': RequestIndication,
            'session_ambr': Ambr,
            'qos_flows_add_mod_request_list': List[QosFlowAddModifyRequestItem],
            'qos_flows_rel_request_list': List[QosFlowReleaseRequestItem],
            'eps_bearer_info': List[EpsBearerInfo],
            'assign_ebi_list': List[EpsBearerId],
            'revoke_ebi_list': List[EpsBearerId],
            'modified_ebi_list': List[EbiArpMapping],
            'pti': ProcedureTransactionId,
            'n1_sm_info_to_ue': RefToBinaryData,
            'always_on_granted': bool,
            'hsmf_pdu_session_uri': Uri,
            'supported_features': SupportedFeatures,
            'cause': Cause,
            'n1sm_cause': str,
            'back_off_timer': DurationSec
        }

        self.attribute_map = {
            'request_indication': 'requestIndication',
            'session_ambr': 'sessionAmbr',
            'qos_flows_add_mod_request_list': 'qosFlowsAddModRequestList',
            'qos_flows_rel_request_list': 'qosFlowsRelRequestList',
            'eps_bearer_info': 'epsBearerInfo',
            'assign_ebi_list': 'assignEbiList',
            'revoke_ebi_list': 'revokeEbiList',
            'modified_ebi_list': 'modifiedEbiList',
            'pti': 'pti',
            'n1_sm_info_to_ue': 'n1SmInfoToUe',
            'always_on_granted': 'alwaysOnGranted',
            'hsmf_pdu_session_uri': 'hsmfPduSessionUri',
            'supported_features': 'supportedFeatures',
            'cause': 'cause',
            'n1sm_cause': 'n1smCause',
            'back_off_timer': 'backOffTimer'
        }
        self._request_indication = request_indication
        self._session_ambr = session_ambr
        self._qos_flows_add_mod_request_list = qos_flows_add_mod_request_list
        self._qos_flows_rel_request_list = qos_flows_rel_request_list
        self._eps_bearer_info = eps_bearer_info
        self._assign_ebi_list = assign_ebi_list
        self._revoke_ebi_list = revoke_ebi_list
        self._modified_ebi_list = modified_ebi_list
        self._pti = pti
        self._n1_sm_info_to_ue = n1_sm_info_to_ue
        self._always_on_granted = always_on_granted
        self._hsmf_pdu_session_uri = hsmf_pdu_session_uri
        self._supported_features = supported_features
        self._cause = cause
        self._n1sm_cause = n1sm_cause
        self._back_off_timer = back_off_timer

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VsmfUpdateData of this VsmfUpdateData.  # noqa: E501
        :rtype: VsmfUpdateData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request_indication(self):
        """Gets the request_indication of this VsmfUpdateData.


        :return: The request_indication of this VsmfUpdateData.
        :rtype: RequestIndication
        """
        return self._request_indication

    @request_indication.setter
    def request_indication(self, request_indication):
        """Sets the request_indication of this VsmfUpdateData.


        :param request_indication: The request_indication of this VsmfUpdateData.
        :type request_indication: RequestIndication
        """
        if request_indication is None:
            raise ValueError("Invalid value for `request_indication`, must not be `None`")  # noqa: E501

        self._request_indication = request_indication

    @property
    def session_ambr(self):
        """Gets the session_ambr of this VsmfUpdateData.


        :return: The session_ambr of this VsmfUpdateData.
        :rtype: Ambr
        """
        return self._session_ambr

    @session_ambr.setter
    def session_ambr(self, session_ambr):
        """Sets the session_ambr of this VsmfUpdateData.


        :param session_ambr: The session_ambr of this VsmfUpdateData.
        :type session_ambr: Ambr
        """

        self._session_ambr = session_ambr

    @property
    def qos_flows_add_mod_request_list(self):
        """Gets the qos_flows_add_mod_request_list of this VsmfUpdateData.


        :return: The qos_flows_add_mod_request_list of this VsmfUpdateData.
        :rtype: List[QosFlowAddModifyRequestItem]
        """
        return self._qos_flows_add_mod_request_list

    @qos_flows_add_mod_request_list.setter
    def qos_flows_add_mod_request_list(self, qos_flows_add_mod_request_list):
        """Sets the qos_flows_add_mod_request_list of this VsmfUpdateData.


        :param qos_flows_add_mod_request_list: The qos_flows_add_mod_request_list of this VsmfUpdateData.
        :type qos_flows_add_mod_request_list: List[QosFlowAddModifyRequestItem]
        """

        self._qos_flows_add_mod_request_list = qos_flows_add_mod_request_list

    @property
    def qos_flows_rel_request_list(self):
        """Gets the qos_flows_rel_request_list of this VsmfUpdateData.


        :return: The qos_flows_rel_request_list of this VsmfUpdateData.
        :rtype: List[QosFlowReleaseRequestItem]
        """
        return self._qos_flows_rel_request_list

    @qos_flows_rel_request_list.setter
    def qos_flows_rel_request_list(self, qos_flows_rel_request_list):
        """Sets the qos_flows_rel_request_list of this VsmfUpdateData.


        :param qos_flows_rel_request_list: The qos_flows_rel_request_list of this VsmfUpdateData.
        :type qos_flows_rel_request_list: List[QosFlowReleaseRequestItem]
        """

        self._qos_flows_rel_request_list = qos_flows_rel_request_list

    @property
    def eps_bearer_info(self):
        """Gets the eps_bearer_info of this VsmfUpdateData.


        :return: The eps_bearer_info of this VsmfUpdateData.
        :rtype: List[EpsBearerInfo]
        """
        return self._eps_bearer_info

    @eps_bearer_info.setter
    def eps_bearer_info(self, eps_bearer_info):
        """Sets the eps_bearer_info of this VsmfUpdateData.


        :param eps_bearer_info: The eps_bearer_info of this VsmfUpdateData.
        :type eps_bearer_info: List[EpsBearerInfo]
        """

        self._eps_bearer_info = eps_bearer_info

    @property
    def assign_ebi_list(self):
        """Gets the assign_ebi_list of this VsmfUpdateData.


        :return: The assign_ebi_list of this VsmfUpdateData.
        :rtype: List[EpsBearerId]
        """
        return self._assign_ebi_list

    @assign_ebi_list.setter
    def assign_ebi_list(self, assign_ebi_list):
        """Sets the assign_ebi_list of this VsmfUpdateData.


        :param assign_ebi_list: The assign_ebi_list of this VsmfUpdateData.
        :type assign_ebi_list: List[EpsBearerId]
        """

        self._assign_ebi_list = assign_ebi_list

    @property
    def revoke_ebi_list(self):
        """Gets the revoke_ebi_list of this VsmfUpdateData.


        :return: The revoke_ebi_list of this VsmfUpdateData.
        :rtype: List[EpsBearerId]
        """
        return self._revoke_ebi_list

    @revoke_ebi_list.setter
    def revoke_ebi_list(self, revoke_ebi_list):
        """Sets the revoke_ebi_list of this VsmfUpdateData.


        :param revoke_ebi_list: The revoke_ebi_list of this VsmfUpdateData.
        :type revoke_ebi_list: List[EpsBearerId]
        """

        self._revoke_ebi_list = revoke_ebi_list

    @property
    def modified_ebi_list(self):
        """Gets the modified_ebi_list of this VsmfUpdateData.


        :return: The modified_ebi_list of this VsmfUpdateData.
        :rtype: List[EbiArpMapping]
        """
        return self._modified_ebi_list

    @modified_ebi_list.setter
    def modified_ebi_list(self, modified_ebi_list):
        """Sets the modified_ebi_list of this VsmfUpdateData.


        :param modified_ebi_list: The modified_ebi_list of this VsmfUpdateData.
        :type modified_ebi_list: List[EbiArpMapping]
        """

        self._modified_ebi_list = modified_ebi_list

    @property
    def pti(self):
        """Gets the pti of this VsmfUpdateData.


        :return: The pti of this VsmfUpdateData.
        :rtype: ProcedureTransactionId
        """
        return self._pti

    @pti.setter
    def pti(self, pti):
        """Sets the pti of this VsmfUpdateData.


        :param pti: The pti of this VsmfUpdateData.
        :type pti: ProcedureTransactionId
        """

        self._pti = pti

    @property
    def n1_sm_info_to_ue(self):
        """Gets the n1_sm_info_to_ue of this VsmfUpdateData.


        :return: The n1_sm_info_to_ue of this VsmfUpdateData.
        :rtype: RefToBinaryData
        """
        return self._n1_sm_info_to_ue

    @n1_sm_info_to_ue.setter
    def n1_sm_info_to_ue(self, n1_sm_info_to_ue):
        """Sets the n1_sm_info_to_ue of this VsmfUpdateData.


        :param n1_sm_info_to_ue: The n1_sm_info_to_ue of this VsmfUpdateData.
        :type n1_sm_info_to_ue: RefToBinaryData
        """

        self._n1_sm_info_to_ue = n1_sm_info_to_ue

    @property
    def always_on_granted(self):
        """Gets the always_on_granted of this VsmfUpdateData.


        :return: The always_on_granted of this VsmfUpdateData.
        :rtype: bool
        """
        return self._always_on_granted

    @always_on_granted.setter
    def always_on_granted(self, always_on_granted):
        """Sets the always_on_granted of this VsmfUpdateData.


        :param always_on_granted: The always_on_granted of this VsmfUpdateData.
        :type always_on_granted: bool
        """

        self._always_on_granted = always_on_granted

    @property
    def hsmf_pdu_session_uri(self):
        """Gets the hsmf_pdu_session_uri of this VsmfUpdateData.


        :return: The hsmf_pdu_session_uri of this VsmfUpdateData.
        :rtype: Uri
        """
        return self._hsmf_pdu_session_uri

    @hsmf_pdu_session_uri.setter
    def hsmf_pdu_session_uri(self, hsmf_pdu_session_uri):
        """Sets the hsmf_pdu_session_uri of this VsmfUpdateData.


        :param hsmf_pdu_session_uri: The hsmf_pdu_session_uri of this VsmfUpdateData.
        :type hsmf_pdu_session_uri: Uri
        """

        self._hsmf_pdu_session_uri = hsmf_pdu_session_uri

    @property
    def supported_features(self):
        """Gets the supported_features of this VsmfUpdateData.


        :return: The supported_features of this VsmfUpdateData.
        :rtype: SupportedFeatures
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this VsmfUpdateData.


        :param supported_features: The supported_features of this VsmfUpdateData.
        :type supported_features: SupportedFeatures
        """

        self._supported_features = supported_features

    @property
    def cause(self):
        """Gets the cause of this VsmfUpdateData.


        :return: The cause of this VsmfUpdateData.
        :rtype: Cause
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this VsmfUpdateData.


        :param cause: The cause of this VsmfUpdateData.
        :type cause: Cause
        """

        self._cause = cause

    @property
    def n1sm_cause(self):
        """Gets the n1sm_cause of this VsmfUpdateData.


        :return: The n1sm_cause of this VsmfUpdateData.
        :rtype: str
        """
        return self._n1sm_cause

    @n1sm_cause.setter
    def n1sm_cause(self, n1sm_cause):
        """Sets the n1sm_cause of this VsmfUpdateData.


        :param n1sm_cause: The n1sm_cause of this VsmfUpdateData.
        :type n1sm_cause: str
        """

        self._n1sm_cause = n1sm_cause

    @property
    def back_off_timer(self):
        """Gets the back_off_timer of this VsmfUpdateData.


        :return: The back_off_timer of this VsmfUpdateData.
        :rtype: DurationSec
        """
        return self._back_off_timer

    @back_off_timer.setter
    def back_off_timer(self, back_off_timer):
        """Sets the back_off_timer of this VsmfUpdateData.


        :param back_off_timer: The back_off_timer of this VsmfUpdateData.
        :type back_off_timer: DurationSec
        """

        self._back_off_timer = back_off_timer