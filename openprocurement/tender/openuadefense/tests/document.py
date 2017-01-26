# -*- coding: utf-8 -*-
import unittest
from email.header import Header
from openprocurement.api.tests.base import create_classmethod
from openprocurement.tender.openuadefense.tests.base import BaseTenderUAContentWebTest
from openprocurement.api.tests.document_test_utils import (not_found,
                                                           put_tender_document,
                                                           patch_tender_document,
                                                           create_tender_document,
                                                           create_tender_document_json_invalid,
                                                           create_tender_document_json,
                                                           put_tender_document_json)

class TenderDocumentResourceTest(BaseTenderUAContentWebTest):
    docservice = False
    status = 'active_auction'
    test_not_found = create_classmethod(not_found)
    test_put_tender_document = create_classmethod(put_tender_document)
    test_patch_tender_document = create_classmethod(patch_tender_document)
    test_create_tender_document = create_classmethod(create_tender_document)


class TenderDocumentWithDSResourceTest(TenderDocumentResourceTest):
    docservice = True
    test_create_tender_document_json_invalid = create_classmethod(create_tender_document_json_invalid)
    test_create_tender_document_json = create_classmethod(create_tender_document_json)
    test_put_tender_document_json = create_classmethod(put_tender_document_json)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderDocumentResourceTest))
    suite.addTest(unittest.makeSuite(TenderDocumentWithDSResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
