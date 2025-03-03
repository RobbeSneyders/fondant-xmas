"""This component filters images of the dataset based on image size
(minimum image size and maximumn aspect ratio).
"""
import logging

import numpy as np
import pandas as pd
from fondant.component import PandasTransformComponent

logger = logging.getLogger(__name__)


class FilterImageResolutionComponent(PandasTransformComponent):
    """Component that filters images based on height and width."""

    def __init__(
        self,
        *,
        min_image_dim: int,
        max_aspect_ratio: float,
        **kwargs,
    ) -> None:
        """
        Args:
            min_image_dim: minimum image dimension.
            max_aspect_ratio: maximum aspect ratio.
            kwargs: Unhandled keyword arguments passed in by Fondant.
        """
        self.min_image_dim = min_image_dim
        self.max_aspect_ratio = max_aspect_ratio

    def transform(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        width = dataframe["image_width"]
        height = dataframe["image_height"]
        min_image_dim = np.minimum(width, height)
        max_image_dim = np.maximum(width, height)
        aspect_ratio = max_image_dim / min_image_dim
        mask = (min_image_dim >= self.min_image_dim) & (
            aspect_ratio <= self.max_aspect_ratio
        )

        return dataframe[mask]
