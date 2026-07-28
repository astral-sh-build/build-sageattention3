import importlib
from importlib.metadata import version

import pytest
import torch


@pytest.fixture(scope="module")
def device() -> torch.device:
    assert torch.cuda.is_available(), "The tests must run on a CUDA GPU"
    device = torch.device("cuda")
    assert torch.cuda.get_device_capability(device)[0] >= 10
    return device


def test_published_cuda_wheel(device: torch.device) -> None:
    assert version("sageattn3") == "2.2.0+cu.12.8.torch.2.10"
    assert torch.__version__ == "2.10.0+cu128"
    assert torch.version.cuda == "12.8"
    assert torch.cuda.get_device_name(device)


@pytest.mark.parametrize("module_name", ["sageattn3"])
def test_native_module(device: torch.device, module_name: str) -> None:
    assert importlib.import_module(module_name) is not None


@pytest.mark.parametrize("causal", [False, True])
def test_blackwell_fp4_attention(device: torch.device, causal: bool) -> None:
    from sageattn3 import sageattn3_blackwell

    torch.manual_seed(0)
    query, key, value = (
        torch.randn((1, 4, 128, 64), device=device, dtype=torch.bfloat16)
        for _ in range(3)
    )
    if torch.cuda.get_device_capability(device) != (12, 0):
        with pytest.raises(RuntimeError, match="only supports Blackwell GPUs"):
            sageattn3_blackwell(query, key, value, is_causal=causal)
        return

    actual = sageattn3_blackwell(query, key, value, is_causal=causal)
    expected = torch.nn.functional.scaled_dot_product_attention(
        query.float(), key.float(), value.float(), is_causal=causal
    ).to(query.dtype)
    assert actual.shape == expected.shape
    assert torch.isfinite(actual).all()
    torch.testing.assert_close(actual, expected, atol=0.35, rtol=0.35)
