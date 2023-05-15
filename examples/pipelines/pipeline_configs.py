"""Dataset creation pipeline config"""
import os

from dataclasses import dataclass


@dataclass
class PipelineConfigs:
    """
    General Pipeline Configs
    Params:
        ARTIFACT_BUCKET (str): the GCS bucket used to store the artifacts
        HOST (str): the kfp host url
    """

    BASE_PATH = "gs://soy-audio-379412_kfp-artifacts/custom_artifact"
    HOST = "https://52074149b1563463-dot-europe-west1.pipelines.googleusercontent.com/"
