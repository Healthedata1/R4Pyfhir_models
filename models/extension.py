#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Extension) on 2018-12-23.
#  2018, SMART Health IT.


from . import element

class Extension(element.Element):
    """ Optional Extensions Element.
    
    Optional Extension Element - found in all resources.
    """
    
    resource_type = "Extension"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        
        """ identifies the meaning of the extension.
        Type `str`. """
        
        self.valueAddress = None
        
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        
        """ Value of extension.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        
        """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueBase64Binary = None
        
        """ extension for fhir primitive  valueBase64Binary"""
        
        self.valueBoolean = None
        
        """ Value of extension.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCanonical = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueCanonical = None
        
        """ extension for fhir primitive  valueCanonical"""
        
        self.valueCode = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueCodeableConcept = None
        
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        
        """ Value of extension.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        
        """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        
        """ Value of extension.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        
        """ Value of extension.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        
        """ Value of extension.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueDate = None
        
        """ extension for fhir primitive  valueDate"""
        
        self.valueDateTime = None
        
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueDateTime = None
        
        """ extension for fhir primitive  valueDateTime"""
        
        self.valueDecimal = None
        
        """ Value of extension.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueDistance = None
        
        """ Value of extension.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        
        """ Value of extension.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        
        """ Value of extension.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        
        """ Value of extension.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueId = None
        
        """ extension for fhir primitive  valueId"""
        
        self.valueIdentifier = None
        
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueInstant = None
        
        """ extension for fhir primitive  valueInstant"""
        
        self.valueInteger = None
        
        """ Value of extension.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueMarkdown = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueMarkdown = None
        
        """ extension for fhir primitive  valueMarkdown"""
        
        self.valueMoney = None
        
        """ Value of extension.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueOid = None
        
        """ extension for fhir primitive  valueOid"""
        
        self.valueParameterDefinition = None
        
        """ Value of extension.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        
        """ Value of extension.
        Type `int`. """
        
        self._valuePositiveInt = None
        
        """ extension for fhir primitive  valuePositiveInt"""
        
        self.valueQuantity = None
        
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        
        """ Value of extension.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        
        """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        
        """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueTime = None
        
        """ extension for fhir primitive  valueTime"""
        
        self.valueTiming = None
        
        """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        
        """ Value of extension.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        
        """ Value of extension.
        Type `int`. """
        
        self._valueUnsignedInt = None
        
        """ extension for fhir primitive  valueUnsignedInt"""
        
        self.valueUri = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        self.valueUrl = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueUrl = None
        
        """ extension for fhir primitive  valueUrl"""
        
        self.valueUsageContext = None
        
        """ Value of extension.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        
        """ Value of extension.
        Type `str`. """
        
        self._valueUuid = None
        
        """ extension for fhir primitive  valueUuid"""
        
        super(Extension, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", False),
            ("valueAge", "valueAge", age.Age, False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("_valueBase64Binary", "_valueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", False),
            ("_valueCanonical", "_valueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", False),
            ("valueCount", "valueCount", count.Count, False, "value", False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", False),
            ("valueDate", "valueDate", FHIRDate, False, "value", False),
            ("_valueDate", "_valueDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("_valueDateTime", "_valueDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("_valueId", "_valueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("valueInstant", "valueInstant", FHIRDate, False, "value", False),
            ("_valueInstant", "_valueInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("_valueMarkdown", "_valueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("_valueOid", "_valueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("_valuePositiveInt", "_valuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
            ("_valueTime", "_valueTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("_valueUnsignedInt", "_valueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", False),
            ("_valueUrl", "_valueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", False),
            ("valueUuid", "valueUuid", str, False, "value", False),
            ("_valueUuid", "_valueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext
from . import fhirprimitive

