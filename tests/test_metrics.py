"""Metrik birim testleri — artefakt regresyonunu engeller."""
import numpy as np
import pytest
from evaluation.metrics import noon_ratio, coverage, pinball


def test_noon_ratio_zero_denominator():
    q01 = np.array([0.1, 0.2, 0.3])
    q05 = np.array([0.0001, 0.0001, 0.0001])
    mask = np.array([True, True, True])
    result = noon_ratio(q01, q05, mask, eps=1e-3)
    assert np.isnan(result)


def test_noon_ratio_normal():
    q01 = np.array([0.5, 0.6, 0.7])
    q05 = np.array([1.0, 1.2, 1.4])
    mask = np.array([True, True, True])
    result = noon_ratio(q01, q05, mask)
    assert 0.4 < result < 0.7


def test_coverage_perfect():
    actual = np.array([0.5, 0.6, 0.7])
    assert coverage(actual, np.zeros(3), np.ones(3)) == 1.0


def test_pinball_symmetry():
    actual = np.array([1.0, 2.0, 3.0])
    pred = np.array([1.5, 1.5, 2.5])
    pb = pinball(actual, pred, quantile=0.5)
    expected = np.mean(np.abs(actual - pred)) / 2
    assert abs(pb - expected) < 1e-9
