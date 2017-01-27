# -*- coding: utf-8 -*-
import unittest
from datetime import timedelta

from openprocurement.api.models import get_now
from openprocurement.api.tests.base import test_organization, create_classmethod
from openprocurement.tender.openua.tests.base import test_bids
from openprocurement.tender.openua.tests.contract_test_utils import (
    create_tender_contract,
    patch_tender_contract
)
from openprocurement.tender.openuadefense.tests.base import BaseTenderUAContentWebTest, test_tender_data
from openprocurement.api.tests.contract_test_utils import (
    create_tender_contract_invalid,
    get_tender_contract,
    get_tender_contracts,
    not_found,
    create_tender_contract_document,
    put_tender_contract_document,
    patch_tender_contract_document
)

class TenderContractResourceTest(BaseTenderUAContentWebTest):
    #initial_data = tender_data
    initial_status = 'active.qualification'
    initial_bids = test_bids
    test_create_tender_contract_invalid = create_classmethod(create_tender_contract_invalid)
    test_get_tender_contract = create_classmethod(get_tender_contract)
    test_get_tender_contracts = create_classmethod(get_tender_contracts)
    test_create_tender_contract = create_classmethod(create_tender_contract)
    test_patch_tender_contract = create_classmethod(patch_tender_contract)
    def setUp(self):
        super(TenderContractResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/tenders/{}/awards'.format(
            self.tender_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id'],
                                       'value': self.initial_bids[0]['value']}})
        award = response.json['data']
        self.award_id = award['id']
        response = self.app.patch_json('/tenders/{}/awards/{}'.format(self.tender_id, self.award_id), {"data": {"status": "active", "qualified": True, "eligible": True}})



class TenderContractDocumentResourceTest(BaseTenderUAContentWebTest):
    #initial_data = tender_data
    initial_status = 'active.qualification'
    initial_bids = test_bids
    status = 'unsuccessful'

    def setUp(self):
        super(TenderContractDocumentResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/tenders/{}/awards'.format(
            self.tender_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.award_id = award['id']
        response = self.app.patch_json('/tenders/{}/awards/{}'.format(self.tender_id, self.award_id), {"data": {"status": "active", "qualified": True, "eligible": True}})
        # Create contract for award
        response = self.app.post_json('/tenders/{}/contracts'.format(self.tender_id), {'data': {'title': 'contract title', 'description': 'contract description', 'awardID': self.award_id}})
        contract = response.json['data']
        self.contract_id = contract['id']

    test_not_found = create_classmethod(not_found)
    test_create_tender_contract_document = create_classmethod(create_tender_contract_document)
    test_put_tender_contract_document = create_classmethod(put_tender_contract_document)
    test_patch_tender_contract_document = create_classmethod(patch_tender_contract_document)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderContractResourceTest))
    suite.addTest(unittest.makeSuite(TenderContractDocumentResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
