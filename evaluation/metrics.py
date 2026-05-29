"""Değerlendirme metrikleri — MAE, RMSE, Pinball, CRPS, Coverage, Pearson r, noon_ratio."""
import numpy as np
from scipy import stats


def mae(actual: np.ndarray, predicted: np.ndarray) -> float:
    return float(np.mean(np.abs(actual - predicted)))


def rmse(actual: np.ndarray, predicted: np.ndarray) -> float:
    return float(np.sqrt(np.mean((actual - predicted) ** 2)))


def pinball(actual: np.ndarray, predicted: np.ndarray, quantile: float) -> float:
    err = actual - predicted
    return float(np.mean(np.where(err >= 0, quantile * err, (quantile - 1) * err)))


def coverage(actual: np.ndarray, q_lo: np.ndarray, q_hi: np.ndarray) -> float:
    return float(np.mean((actual >= q_lo) & (actual <= q_hi)))


def crps_gaussian(actual: np.ndarray, mu: np.ndarray, sigma: np.ndarray) -> float:
    z = (actual - mu) / (sigma + 1e-8)
    phi = stats.norm.pdf(z)
    Phi = stats.norm.cdf(z)
    return float(np.mean(sigma * (z * (2 * Phi - 1) + 2 * phi - 1 / np.sqrt(np.pi))))


def pearson_q50(actual: np.ndarray, q50: np.ndarray) -> float:
    """Şekil yakalama tanı metriği."""
    r, _ = stats.pearsonr(actual, q50)
    return float(r)


def noon_ratio(q01: np.ndarray, q05: np.ndarray, noon_mask: np.ndarray,
               eps: float = 1e-3) -> float:
    """q01/q05 oranı — sıfıra-yakın bölme korumalı."""
    q01_n = q01[noon_mask]
    q05_n = q05[noon_mask]
    valid = q05_n > eps
    if valid.sum() == 0:
        return float("nan")
    return float(np.nanmean(np.where(valid, q01_n / q05_n, np.nan)))
