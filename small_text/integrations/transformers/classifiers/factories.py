from small_text.classifiers.factories import AbstractClassifierFactory
from small_text.integrations.transformers.classifiers.classification import (
    TransformerBasedClassification,
)

from small_text.integrations.transformers.classifiers.uncertainty_base_class import (
    BayesianUncertaintyClassifier,
    EnsemblesUncertaintyClassifier,
    EvidentialDeepLearning1UncertaintyClassifier,
    EvidentialDeepLearning2UncertaintyClassifier,
    InhibitedSoftmaxUncertaintyClassifier,
    LabelSmoothingUncertaintyClassifier,
    ModelCalibrationUncertaintyClassifier,
    MonteCarloDropoutUncertaintyClassifier,
    SoftmaxUncertaintyClassifier,
    TemperatureScalingUncertaintyClassifier,
    TrustScoreUncertaintyClassifier,
)


class TransformerBasedClassificationFactory(AbstractClassifierFactory):
    def __init__(self, transformer_model, num_classes, kwargs={}):
        self.transformer_model = transformer_model
        self.num_classes = num_classes
        self.kwargs = kwargs

    def new(self):
        return TransformerBasedClassification(
            self.transformer_model, self.num_classes, **self.kwargs
        )


class UncertaintyBasedClassificationFactory(TransformerBasedClassificationFactory):
    def __init__(
        self, transformer_model, num_classes, uncertainty_method="softmax", kwargs={}
    ):
        self.uncertainty_method = uncertainty_method
        super().__init__(transformer_model, num_classes, kwargs)

    def new(self):
        match self.uncertainty_method:
            case "softmax":
                return SoftmaxUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "temp_scaling":
                return TemperatureScalingUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "label_smoothing":
                return LabelSmoothingUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "MonteCarlo":
                return MonteCarloDropoutUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "inhibited":
                return InhibitedSoftmaxUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "evidential1":
                return EvidentialDeepLearning1UncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "evidential2":
                return EvidentialDeepLearning2UncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "bayesian":
                return BayesianUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "ensembles":
                return EnsemblesUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "trustscore":
                return TrustScoreUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case "model_calibration":
                return ModelCalibrationUncertaintyClassifier(
                    self.transformer_model, self.num_classes, **self.kwargs
                )
            case _:
                return super().new()
