#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Unit tests for the NLTK maximum entropy entity extraction methods.

This module implements unit tests for the named entity extraction functionality in English based on the
NLTK POS-tagging and (fuzzy) chunking methods.

Todo:
    * Better testing for exact test in return sources
    * More pathological and difficult cases
"""
from nose.tools import assert_equal

from lexnlp.extract.en.entities.nltk_maxent import get_noun_phrases, get_companies, get_persons, get_geopolitical, \
    get_organizations
from lexnlp.tests import lexnlp_tests

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2017, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "0.1.6"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


def test_noun_phrases():
    """
    Test get_noun_phrases methods.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_noun_phrases)


def test_companies():
    """
    Test get_companies methods.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_companies,
                                                   actual_data_converter=lambda actual: [(c[0], c[1]) for c in actual])


def test_companies_count():
    """
    Test get_companies with counting uniques.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_companies, detail_type=True, count_unique=True,
                                                   actual_data_converter=lambda actual: [(c[0], c[2], str(c[-1]))
                                                                                         for c in actual])


def test_company_upper_name():
    """
    Test get_companies methods with name_upper arg.
    :return:
    """
    # Example text
    example = 'This organization Ibm INC should be uppercased'
    results = {('IBM', 'INC')}
    lexnlp_tests.test_extraction_func(results, get_companies, example, name_upper=True)


def test_companies_rs():
    """
    Test get_companies methods with return_source.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_companies, return_source=True,
                                                   actual_data_converter=lambda actual: [(c[0], c[1]) for c in actual])


def test_companies_and():
    """
    Test get_companies methods with CC case.
    :return:
    """
    # Example text
    example = 'Those two organizations IBM INC and LexPredict LLC are cool.'
    results = {('IBM', 'INC'),
               ('LexPredict', 'LLC')}
    lexnlp_tests.test_extraction_func(results, get_companies, example)


def test_company_has_type_only():
    """
    Test get_companies methods with company without name.
    :return:
    """
    # Example text
    example = 'Those two organizations IBM INC and company without name LLC are cool.'
    results = {('IBM', 'INC')}
    lexnlp_tests.test_extraction_func(results, get_companies, example)


def test_company_detail_type():
    """
    Test get_companies methods with detailed type option.
    :return:
    """
    # Example text
    example = 'Those two organizations IBM INC and LexPredict LLC are cool.'
    results = [('IBM', 'INC', 'CORP', 'Corporation', None),
               ('LexPredict', 'LLC', 'LLC', 'Company', None)]
    lexnlp_tests.test_extraction_func(results, get_companies, example,
                                      detail_type=True)


def test_company_abbr_name():
    """
    Test get_companies methods with detailed type option.
    :return:
    """
    # Example text
    example = 'Those two organizations IBM INC and LexPredict LLC (LP) are cool.'
    results = [('IBM', 'INC', None),
               ('LexPredict', 'LLC', 'LP')]
    lexnlp_tests.test_extraction_func(results, get_companies, example,
                                      parse_name_abbr=True)


def test_persons():
    """
    Test get_persons methods.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_persons)


def test_persons_rs():
    """
    Test get_persons methods with return_source.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_persons, return_source=True,
                                                   actual_data_converter=lambda actual: [p[0] for p in actual])


def test_gpes():
    """
    Test get_geopolitical methods.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_geopolitical)


def test_gpes_rs():
    """
    Test get_geopolitical methods with return_source
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_geopolitical, return_source=True,
                                                   actual_data_converter=lambda actual: [v[0] for v in actual])


def test_orgs():
    """
    Test get_organizations methods.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_organizations)


def test_orgs_rs():
    """
    Test get_organizations methods with return_source.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_organizations, return_source=True,
                                                   actual_data_converter=lambda actual: [v[0] for v in actual])


def test_orgs_or():
    """
    Test get_organizations methods with CC case.
    :return:
    """
    orgs = list(get_organizations("We will work with either Acme Inc. or Beta Co."))
    num_orgs = len(orgs)
    assert_equal(num_orgs, 2)


def test_orgs_and():
    """
    Test get_organizations methods with CC case.
    :return:
    """
    orgs = list(get_organizations("We will work with either Acme Inc. and Beta Co."))
    num_orgs = len(orgs)
    assert_equal(num_orgs, 1)


def test_person_in():
    """
    Test whether large list of person examples match.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_persons,
                                                   test_only_expected_in=True)


def test_gpe_in():
    """
    Test whether large list of GPE examples match.
    :return:
    """
    lexnlp_tests.test_extraction_func_on_test_data(get_geopolitical,
                                                   test_only_expected_in=True)
