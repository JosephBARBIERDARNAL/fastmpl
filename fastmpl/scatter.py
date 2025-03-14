import matplotlib.pyplot as plt
import narwhals as nw
from narwhals.typing import IntoDataFrame
from typing import Union


def fastscatter(
    x: str,
    y: str,
    data: IntoDataFrame,
    color: str = "#72874E",
    edgecolor: str = "#023743",
    s: Union[str, int] = None,
):
    df = nw.from_native(data)
    x = df.select(x)
    y = df.select(y)

    if s is not None:
        if isinstance(s, str):
            s = df.select(s)

    scheme = """
B.
AC
"""
    fig, axs = plt.subplot_mosaic(
        mosaic=scheme,
        figsize=(10, 8),
        width_ratios=(5, 1),
        height_ratios=(1, 5),
        dpi=300,
    )
    fig.subplots_adjust(wspace=0, hspace=0)

    axs["A"].scatter(
        x=x,
        y=y,
        s=s,
        color=color,
        edgecolor=edgecolor,
        alpha=0.7,
        zorder=10,
    )

    axs["A"].grid(color="#525252", alpha=0.2, zorder=-1)
    axs["A"].spines[["top", "right", "left", "bottom"]].set_visible(False)
    axs["A"].tick_params(size=0, labelsize=10)

    axs["B"].hist(x, bins=20, color=color, edgecolor=edgecolor)
    axs["C"].hist(
        y, orientation="horizontal", bins=20, color=color, edgecolor=edgecolor
    )

    axs["B"].axis("off")
    axs["C"].axis("off")

    return fig, axs


if __name__ == "__main__":
    import numpy as np
    import pandas as pd

    np.random.seed(123)

    x = np.random.normal(size=500)
    y = x * 0.05 + np.random.normal(size=500)
    df = pd.DataFrame({"x": x, "y": y})

    fig, _ = fastscatter("x", "y", df, s=100)
    fig.savefig("cache.png", dpi=300)
