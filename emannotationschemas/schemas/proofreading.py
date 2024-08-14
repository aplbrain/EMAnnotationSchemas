from emannotationschemas.schemas.base import (
    AnnotationSchema,
    BoundSpatialPoint,
    NumericField,
)
from marshmallow import fields, validate

proofread_choices = ["non", "clean", "extended"]
options_text = "Options are: 'non' to indicate no comprehensive proofreading, 'clean' to indicate comprehensive removal of false merges, and 'extended' to mean comprehensive extension of neurite tips"


class PointWithValid(AnnotationSchema):
    pt = fields.Nested(
        BoundSpatialPoint,
        required=True,
        description="Core location on proofread object",
    )
    valid_id = NumericField(
        required=True,
        description="Root id of the object when proofread status was assigned. If the pt_root_id of the cell differs, the proofreading status may not apply.",
    )


class ProofreadStatus(PointWithValid):
    status = fields.String(
        required=True,
        validate=validate.OneOf(proofread_choices),
        description=f"Proofread status of cell. {options_text}",
    )


class CompartmentProofreadStatus(PointWithValid):
    status_dendrite = fields.String(
        required=True,
        validate=validate.OneOf(proofread_choices),
        description=f"Proofread status of the dendrite only. {options_text}",
    )
    status_axon = fields.String(
        required=True,
        validate=validate.OneOf(proofread_choices),
        description=f"Proofread status of the axon only. {options_text}",
    )


class ProofreadingBoolStatus(PointWithValid):
    proofread = fields.Bool(
        required=True,
        description="Proofread status of cell.",
    )


class ProofreadingBoolStatusUser(ProofreadingBoolStatus):
    user_id = fields.Int(
        required=True,
        description="User who assessed the proofreading status.",
    )

class CompartmentProofreadStatusStrategy(PointWithValid):
    status_dendrite = fields.Bool(
        required=True,
        description=f"Proofread status of the dendrite only. True indicates dendrite is at least clean.",
    )
    status_axon = fields.Bool(
        required=True,
        description=f"Proofread status of the axon only. True indicates axon is at least clean.",
    )
    strategy_dendrite = fields.String(
        required=True,
        description=f"Strategy used when proofreading dendrite. See table description for more details.",
    )
    strategy_axon = fields.String(
        required=True,
        description=f"Strategy used when proofreading axon. See table description for more details.",
    )
    
# Adding classes from https://github.com/aplbrain/BENCHMARK-Metadata/blob/1.1-and-1.2-annotation-metadata-for-review/annotation-metadata/CAVE-implemented-annotation-metadata-version-1.2.plantuml
# With explanations from here: https://github.com/aplbrain/BENCHMARK-Metadata/blob/1.1-and-1.2-annotation-metadata-for-review/annotation-metadata/required-field-names.md

class AnnotationProvenance(PointWithValid):
    valid = fields.Boolean(description="Indicates if the annotation is valid")
    pt = fields.Nested('PointSchema', description="Point schema for location data")
    valid_id = fields.Float(description="Validation ID")
    status = fields.String(description="Status of the annotation")
    

class Annotator(PointWithValid):
    valid = fields.Boolean(description="Indicates if the annotator data is valid")
    pt = fields.Nested('PointSchema', description="Point schema for location data")
    valid_id = fields.Float(description="Validation ID")
    contributor_method = fields.String(description="Method used by the contributor")
    novice_annotator = fields.Boolean(description="Indicates if the annotator is a novice")
    expert_annotator = fields.Boolean(description="Indicates if the annotator is an expert")
    novice_proofreader = fields.Boolean(description="Indicates if the proofreader is a novice")
    expert_proofreader = fields.Boolean(description="Indicates if the proofreader is an expert")
    contributor = fields.String(description="Name of the contributor")
    other = fields.String(description="Other annotator-related information")

class Score(PointWithValid):
    valid = fields.Boolean(description="Indicates if the score is valid")
    pt = fields.Nested('PointSchema', description="Point schema for location data")
    valid_id = fields.Float(description="Validation ID")
    annotation_reviewed = fields.Integer(description="Number of annotations reviewed")
    review_time_hours = fields.Integer(description="Time spent reviewing annotations (in hours)")
    confidence_value = fields.Integer(description="Confidence value of the annotation")
    other = fields.Integer(description="Other score-related information")

class Versioning(PointWithValid):
    valid = fields.Boolean(description="Indicates if the versioning is valid")
    pt = fields.Nested('PointSchema', description="Point schema for location data")
    valid_id = fields.Float(description="Validation ID")
    version_checkpoint_value = fields.Integer(description="Version checkpoint value")
    version_checkpoint_updates = fields.String(description="Updates made in this version")
    other = fields.String(description="Other versioning-related information")