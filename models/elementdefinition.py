#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2018-12-23.
#  2018, SMART Health IT.


from . import backboneelement

class ElementDefinition(backboneelement.BackboneElement):
    """ Definition of an element in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    resource_type = "ElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        
        """ Other names.
        List of `str` items. """
        
        self._alias = None
        
        """ extension for fhir primitive  alias"""
        
        self.base = None
        
        """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """
        
        self.binding = None
        
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Corresponding codes in terminologies.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.comment = None
        
        """ Comments about the use of this element.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.condition = None
        
        """ Reference to invariant about presence.
        List of `str` items. """
        
        self._condition = None
        
        """ extension for fhir primitive  condition"""
        
        self.constraint = None
        
        """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """
        
        self.contentReference = None
        
        """ Reference to definition of content for the element.
        Type `str`. """
        
        self._contentReference = None
        
        """ extension for fhir primitive  contentReference"""
        
        self.defaultValueAddress = None
        
        """ Specified value if missing from instance.
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge = None
        
        """ Specified value if missing from instance.
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation = None
        
        """ Specified value if missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment = None
        
        """ Specified value if missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueBase64Binary = None
        
        """ extension for fhir primitive  defaultValueBase64Binary"""
        
        self.defaultValueBoolean = None
        
        """ Specified value if missing from instance.
        Type `bool`. """
        
        self._defaultValueBoolean = None
        
        """ extension for fhir primitive  defaultValueBoolean"""
        
        self.defaultValueCanonical = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueCanonical = None
        
        """ extension for fhir primitive  defaultValueCanonical"""
        
        self.defaultValueCode = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueCode = None
        
        """ extension for fhir primitive  defaultValueCode"""
        
        self.defaultValueCodeableConcept = None
        
        """ Specified value if missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding = None
        
        """ Specified value if missing from instance.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail = None
        
        """ Specified value if missing from instance.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint = None
        
        """ Specified value if missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueContributor = None
        
        """ Specified value if missing from instance.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueCount = None
        
        """ Specified value if missing from instance.
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement = None
        
        """ Specified value if missing from instance.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueDate = None
        
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._defaultValueDate = None
        
        """ extension for fhir primitive  defaultValueDate"""
        
        self.defaultValueDateTime = None
        
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._defaultValueDateTime = None
        
        """ extension for fhir primitive  defaultValueDateTime"""
        
        self.defaultValueDecimal = None
        
        """ Specified value if missing from instance.
        Type `float`. """
        
        self._defaultValueDecimal = None
        
        """ extension for fhir primitive  defaultValueDecimal"""
        
        self.defaultValueDistance = None
        
        """ Specified value if missing from instance.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDosage = None
        
        """ Specified value if missing from instance.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueDuration = None
        
        """ Specified value if missing from instance.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueExpression = None
        
        """ Specified value if missing from instance.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName = None
        
        """ Specified value if missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueId = None
        
        """ extension for fhir primitive  defaultValueId"""
        
        self.defaultValueIdentifier = None
        
        """ Specified value if missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant = None
        
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._defaultValueInstant = None
        
        """ extension for fhir primitive  defaultValueInstant"""
        
        self.defaultValueInteger = None
        
        """ Specified value if missing from instance.
        Type `int`. """
        
        self._defaultValueInteger = None
        
        """ extension for fhir primitive  defaultValueInteger"""
        
        self.defaultValueMarkdown = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueMarkdown = None
        
        """ extension for fhir primitive  defaultValueMarkdown"""
        
        self.defaultValueMoney = None
        
        """ Specified value if missing from instance.
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValueOid = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueOid = None
        
        """ extension for fhir primitive  defaultValueOid"""
        
        self.defaultValueParameterDefinition = None
        
        """ Specified value if missing from instance.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod = None
        
        """ Specified value if missing from instance.
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt = None
        
        """ Specified value if missing from instance.
        Type `int`. """
        
        self._defaultValuePositiveInt = None
        
        """ extension for fhir primitive  defaultValuePositiveInt"""
        
        self.defaultValueQuantity = None
        
        """ Specified value if missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange = None
        
        """ Specified value if missing from instance.
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio = None
        
        """ Specified value if missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference = None
        
        """ Specified value if missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact = None
        
        """ Specified value if missing from instance.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData = None
        
        """ Specified value if missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature = None
        
        """ Specified value if missing from instance.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueString = None
        
        """ extension for fhir primitive  defaultValueString"""
        
        self.defaultValueTime = None
        
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._defaultValueTime = None
        
        """ extension for fhir primitive  defaultValueTime"""
        
        self.defaultValueTiming = None
        
        """ Specified value if missing from instance.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition = None
        
        """ Specified value if missing from instance.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt = None
        
        """ Specified value if missing from instance.
        Type `int`. """
        
        self._defaultValueUnsignedInt = None
        
        """ extension for fhir primitive  defaultValueUnsignedInt"""
        
        self.defaultValueUri = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueUri = None
        
        """ extension for fhir primitive  defaultValueUri"""
        
        self.defaultValueUrl = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueUrl = None
        
        """ extension for fhir primitive  defaultValueUrl"""
        
        self.defaultValueUsageContext = None
        
        """ Specified value if missing from instance.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueUuid = None
        
        """ Specified value if missing from instance.
        Type `str`. """
        
        self._defaultValueUuid = None
        
        """ extension for fhir primitive  defaultValueUuid"""
        
        self.definition = None
        
        """ Full formal definition as narrative text.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.example = None
        
        """ Example value (as defined for type).
        List of `ElementDefinitionExample` items (represented as `dict` in JSON). """
        
        self.fixedAddress = None
        
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """
        
        self.fixedAge = None
        
        """ Value must be exactly this.
        Type `Age` (represented as `dict` in JSON). """
        
        self.fixedAnnotation = None
        
        """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.fixedAttachment = None
        
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.fixedBase64Binary = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedBase64Binary = None
        
        """ extension for fhir primitive  fixedBase64Binary"""
        
        self.fixedBoolean = None
        
        """ Value must be exactly this.
        Type `bool`. """
        
        self._fixedBoolean = None
        
        """ extension for fhir primitive  fixedBoolean"""
        
        self.fixedCanonical = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedCanonical = None
        
        """ extension for fhir primitive  fixedCanonical"""
        
        self.fixedCode = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedCode = None
        
        """ extension for fhir primitive  fixedCode"""
        
        self.fixedCodeableConcept = None
        
        """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fixedCoding = None
        
        """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.fixedContactDetail = None
        
        """ Value must be exactly this.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.fixedContactPoint = None
        
        """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.fixedContributor = None
        
        """ Value must be exactly this.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.fixedCount = None
        
        """ Value must be exactly this.
        Type `Count` (represented as `dict` in JSON). """
        
        self.fixedDataRequirement = None
        
        """ Value must be exactly this.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.fixedDate = None
        
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._fixedDate = None
        
        """ extension for fhir primitive  fixedDate"""
        
        self.fixedDateTime = None
        
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._fixedDateTime = None
        
        """ extension for fhir primitive  fixedDateTime"""
        
        self.fixedDecimal = None
        
        """ Value must be exactly this.
        Type `float`. """
        
        self._fixedDecimal = None
        
        """ extension for fhir primitive  fixedDecimal"""
        
        self.fixedDistance = None
        
        """ Value must be exactly this.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.fixedDosage = None
        
        """ Value must be exactly this.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.fixedDuration = None
        
        """ Value must be exactly this.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.fixedExpression = None
        
        """ Value must be exactly this.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.fixedHumanName = None
        
        """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.fixedId = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedId = None
        
        """ extension for fhir primitive  fixedId"""
        
        self.fixedIdentifier = None
        
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.fixedInstant = None
        
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._fixedInstant = None
        
        """ extension for fhir primitive  fixedInstant"""
        
        self.fixedInteger = None
        
        """ Value must be exactly this.
        Type `int`. """
        
        self._fixedInteger = None
        
        """ extension for fhir primitive  fixedInteger"""
        
        self.fixedMarkdown = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedMarkdown = None
        
        """ extension for fhir primitive  fixedMarkdown"""
        
        self.fixedMoney = None
        
        """ Value must be exactly this.
        Type `Money` (represented as `dict` in JSON). """
        
        self.fixedOid = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedOid = None
        
        """ extension for fhir primitive  fixedOid"""
        
        self.fixedParameterDefinition = None
        
        """ Value must be exactly this.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.fixedPeriod = None
        
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """
        
        self.fixedPositiveInt = None
        
        """ Value must be exactly this.
        Type `int`. """
        
        self._fixedPositiveInt = None
        
        """ extension for fhir primitive  fixedPositiveInt"""
        
        self.fixedQuantity = None
        
        """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.fixedRange = None
        
        """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """
        
        self.fixedRatio = None
        
        """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.fixedReference = None
        
        """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fixedRelatedArtifact = None
        
        """ Value must be exactly this.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.fixedSampledData = None
        
        """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.fixedSignature = None
        
        """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.fixedString = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedString = None
        
        """ extension for fhir primitive  fixedString"""
        
        self.fixedTime = None
        
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._fixedTime = None
        
        """ extension for fhir primitive  fixedTime"""
        
        self.fixedTiming = None
        
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.fixedTriggerDefinition = None
        
        """ Value must be exactly this.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.fixedUnsignedInt = None
        
        """ Value must be exactly this.
        Type `int`. """
        
        self._fixedUnsignedInt = None
        
        """ extension for fhir primitive  fixedUnsignedInt"""
        
        self.fixedUri = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedUri = None
        
        """ extension for fhir primitive  fixedUri"""
        
        self.fixedUrl = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedUrl = None
        
        """ extension for fhir primitive  fixedUrl"""
        
        self.fixedUsageContext = None
        
        """ Value must be exactly this.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.fixedUuid = None
        
        """ Value must be exactly this.
        Type `str`. """
        
        self._fixedUuid = None
        
        """ extension for fhir primitive  fixedUuid"""
        
        self.isModifier = None
        
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        
        self._isModifier = None
        
        """ extension for fhir primitive  isModifier"""
        
        self.isModifierReason = None
        
        """ Reason that this element is marked as a modifier.
        Type `str`. """
        
        self._isModifierReason = None
        
        """ extension for fhir primitive  isModifierReason"""
        
        self.isSummary = None
        
        """ Include when _summary = true?.
        Type `bool`. """
        
        self._isSummary = None
        
        """ extension for fhir primitive  isSummary"""
        
        self.label = None
        
        """ Name for element to display with or prompt for element.
        Type `str`. """
        
        self._label = None
        
        """ extension for fhir primitive  label"""
        
        self.mapping = None
        
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.max = None
        
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.maxLength = None
        
        """ Max length for strings.
        Type `int`. """
        
        self._maxLength = None
        
        """ extension for fhir primitive  maxLength"""
        
        self.maxValueDate = None
        
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._maxValueDate = None
        
        """ extension for fhir primitive  maxValueDate"""
        
        self.maxValueDateTime = None
        
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._maxValueDateTime = None
        
        """ extension for fhir primitive  maxValueDateTime"""
        
        self.maxValueDecimal = None
        
        """ Maximum Allowed Value (for some types).
        Type `float`. """
        
        self._maxValueDecimal = None
        
        """ extension for fhir primitive  maxValueDecimal"""
        
        self.maxValueInstant = None
        
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._maxValueInstant = None
        
        """ extension for fhir primitive  maxValueInstant"""
        
        self.maxValueInteger = None
        
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self._maxValueInteger = None
        
        """ extension for fhir primitive  maxValueInteger"""
        
        self.maxValuePositiveInt = None
        
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self._maxValuePositiveInt = None
        
        """ extension for fhir primitive  maxValuePositiveInt"""
        
        self.maxValueQuantity = None
        
        """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxValueTime = None
        
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._maxValueTime = None
        
        """ extension for fhir primitive  maxValueTime"""
        
        self.maxValueUnsignedInt = None
        
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self._maxValueUnsignedInt = None
        
        """ extension for fhir primitive  maxValueUnsignedInt"""
        
        self.meaningWhenMissing = None
        
        """ Implicit meaning when this element is missing.
        Type `str`. """
        
        self._meaningWhenMissing = None
        
        """ extension for fhir primitive  meaningWhenMissing"""
        
        self.min = None
        
        """ Minimum Cardinality.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.minValueDate = None
        
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._minValueDate = None
        
        """ extension for fhir primitive  minValueDate"""
        
        self.minValueDateTime = None
        
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._minValueDateTime = None
        
        """ extension for fhir primitive  minValueDateTime"""
        
        self.minValueDecimal = None
        
        """ Minimum Allowed Value (for some types).
        Type `float`. """
        
        self._minValueDecimal = None
        
        """ extension for fhir primitive  minValueDecimal"""
        
        self.minValueInstant = None
        
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._minValueInstant = None
        
        """ extension for fhir primitive  minValueInstant"""
        
        self.minValueInteger = None
        
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self._minValueInteger = None
        
        """ extension for fhir primitive  minValueInteger"""
        
        self.minValuePositiveInt = None
        
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self._minValuePositiveInt = None
        
        """ extension for fhir primitive  minValuePositiveInt"""
        
        self.minValueQuantity = None
        
        """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minValueTime = None
        
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._minValueTime = None
        
        """ extension for fhir primitive  minValueTime"""
        
        self.minValueUnsignedInt = None
        
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self._minValueUnsignedInt = None
        
        """ extension for fhir primitive  minValueUnsignedInt"""
        
        self.mustSupport = None
        
        """ If the element must be supported.
        Type `bool`. """
        
        self._mustSupport = None
        
        """ extension for fhir primitive  mustSupport"""
        
        self.orderMeaning = None
        
        """ What the order of the elements means.
        Type `str`. """
        
        self._orderMeaning = None
        
        """ extension for fhir primitive  orderMeaning"""
        
        self.path = None
        
        """ Path of the element in the hierarchy of elements.
        Type `str`. """
        
        self._path = None
        
        """ extension for fhir primitive  path"""
        
        self.patternAddress = None
        
        """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """
        
        self.patternAge = None
        
        """ Value must have at least these property values.
        Type `Age` (represented as `dict` in JSON). """
        
        self.patternAnnotation = None
        
        """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patternAttachment = None
        
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.patternBase64Binary = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternBase64Binary = None
        
        """ extension for fhir primitive  patternBase64Binary"""
        
        self.patternBoolean = None
        
        """ Value must have at least these property values.
        Type `bool`. """
        
        self._patternBoolean = None
        
        """ extension for fhir primitive  patternBoolean"""
        
        self.patternCanonical = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternCanonical = None
        
        """ extension for fhir primitive  patternCanonical"""
        
        self.patternCode = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternCode = None
        
        """ extension for fhir primitive  patternCode"""
        
        self.patternCodeableConcept = None
        
        """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patternCoding = None
        
        """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patternContactDetail = None
        
        """ Value must have at least these property values.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.patternContactPoint = None
        
        """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.patternContributor = None
        
        """ Value must have at least these property values.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.patternCount = None
        
        """ Value must have at least these property values.
        Type `Count` (represented as `dict` in JSON). """
        
        self.patternDataRequirement = None
        
        """ Value must have at least these property values.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.patternDate = None
        
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._patternDate = None
        
        """ extension for fhir primitive  patternDate"""
        
        self.patternDateTime = None
        
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._patternDateTime = None
        
        """ extension for fhir primitive  patternDateTime"""
        
        self.patternDecimal = None
        
        """ Value must have at least these property values.
        Type `float`. """
        
        self._patternDecimal = None
        
        """ extension for fhir primitive  patternDecimal"""
        
        self.patternDistance = None
        
        """ Value must have at least these property values.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.patternDosage = None
        
        """ Value must have at least these property values.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.patternDuration = None
        
        """ Value must have at least these property values.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.patternExpression = None
        
        """ Value must have at least these property values.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.patternHumanName = None
        
        """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patternId = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternId = None
        
        """ extension for fhir primitive  patternId"""
        
        self.patternIdentifier = None
        
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patternInstant = None
        
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._patternInstant = None
        
        """ extension for fhir primitive  patternInstant"""
        
        self.patternInteger = None
        
        """ Value must have at least these property values.
        Type `int`. """
        
        self._patternInteger = None
        
        """ extension for fhir primitive  patternInteger"""
        
        self.patternMarkdown = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternMarkdown = None
        
        """ extension for fhir primitive  patternMarkdown"""
        
        self.patternMoney = None
        
        """ Value must have at least these property values.
        Type `Money` (represented as `dict` in JSON). """
        
        self.patternOid = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternOid = None
        
        """ extension for fhir primitive  patternOid"""
        
        self.patternParameterDefinition = None
        
        """ Value must have at least these property values.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.patternPeriod = None
        
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """
        
        self.patternPositiveInt = None
        
        """ Value must have at least these property values.
        Type `int`. """
        
        self._patternPositiveInt = None
        
        """ extension for fhir primitive  patternPositiveInt"""
        
        self.patternQuantity = None
        
        """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.patternRange = None
        
        """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """
        
        self.patternRatio = None
        
        """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.patternReference = None
        
        """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patternRelatedArtifact = None
        
        """ Value must have at least these property values.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.patternSampledData = None
        
        """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.patternSignature = None
        
        """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.patternString = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternString = None
        
        """ extension for fhir primitive  patternString"""
        
        self.patternTime = None
        
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._patternTime = None
        
        """ extension for fhir primitive  patternTime"""
        
        self.patternTiming = None
        
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.patternTriggerDefinition = None
        
        """ Value must have at least these property values.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.patternUnsignedInt = None
        
        """ Value must have at least these property values.
        Type `int`. """
        
        self._patternUnsignedInt = None
        
        """ extension for fhir primitive  patternUnsignedInt"""
        
        self.patternUri = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternUri = None
        
        """ extension for fhir primitive  patternUri"""
        
        self.patternUrl = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternUrl = None
        
        """ extension for fhir primitive  patternUrl"""
        
        self.patternUsageContext = None
        
        """ Value must have at least these property values.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.patternUuid = None
        
        """ Value must have at least these property values.
        Type `str`. """
        
        self._patternUuid = None
        
        """ extension for fhir primitive  patternUuid"""
        
        self.representation = None
        
        """ xmlAttr | xmlText | typeAttr | cdaText | xhtml.
        List of `str` items. """
        
        self._representation = None
        
        """ extension for fhir primitive  representation"""
        
        self.requirements = None
        
        """ Why this resource has been created.
        Type `str`. """
        
        self._requirements = None
        
        """ extension for fhir primitive  requirements"""
        
        self.short = None
        
        """ Concise definition for space-constrained presentation.
        Type `str`. """
        
        self._short = None
        
        """ extension for fhir primitive  short"""
        
        self.sliceIsConstraining = None
        
        """ If this slice definition constrains an inherited slice definition
        (or not).
        Type `bool`. """
        
        self._sliceIsConstraining = None
        
        """ extension for fhir primitive  sliceIsConstraining"""
        
        self.sliceName = None
        
        """ Name for this particular element (in a set of slices).
        Type `str`. """
        
        self._sliceName = None
        
        """ extension for fhir primitive  sliceName"""
        
        self.slicing = None
        
        """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        
        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias",fhirprimitive.FHIRPrimitive, False, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("_condition", "_condition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("contentReference", "contentReference", str, False, None, False),
            ("_contentReference", "_contentReference",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("_defaultValueBase64Binary", "_defaultValueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("_defaultValueBoolean", "_defaultValueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("_defaultValueCanonical", "_defaultValueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("_defaultValueCode", "_defaultValueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", FHIRDate, False, "defaultValue", False),
            ("_defaultValueDate", "_defaultValueDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueDateTime", "defaultValueDateTime", FHIRDate, False, "defaultValue", False),
            ("_defaultValueDateTime", "_defaultValueDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("_defaultValueDecimal", "_defaultValueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("_defaultValueId", "_defaultValueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", FHIRDate, False, "defaultValue", False),
            ("_defaultValueInstant", "_defaultValueInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("_defaultValueInteger", "_defaultValueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("_defaultValueMarkdown", "_defaultValueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("_defaultValueOid", "_defaultValueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("_defaultValuePositiveInt", "_defaultValuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("_defaultValueString", "_defaultValueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueTime", "defaultValueTime", FHIRDate, False, "defaultValue", False),
            ("_defaultValueTime", "_defaultValueTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("_defaultValueUnsignedInt", "_defaultValueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("_defaultValueUri", "_defaultValueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("_defaultValueUrl", "_defaultValueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("_defaultValueUuid", "_defaultValueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False),
            ("fixedAge", "fixedAge", age.Age, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("_fixedBase64Binary", "_fixedBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("_fixedBoolean", "_fixedBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("_fixedCanonical", "_fixedCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("_fixedCode", "_fixedCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False),
            ("fixedContactDetail", "fixedContactDetail", contactdetail.ContactDetail, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False),
            ("fixedContributor", "fixedContributor", contributor.Contributor, False, "fixed", False),
            ("fixedCount", "fixedCount", count.Count, False, "fixed", False),
            ("fixedDataRequirement", "fixedDataRequirement", datarequirement.DataRequirement, False, "fixed", False),
            ("fixedDate", "fixedDate", FHIRDate, False, "fixed", False),
            ("_fixedDate", "_fixedDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedDateTime", "fixedDateTime", FHIRDate, False, "fixed", False),
            ("_fixedDateTime", "_fixedDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("_fixedDecimal", "_fixedDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedDistance", "fixedDistance", distance.Distance, False, "fixed", False),
            ("fixedDosage", "fixedDosage", dosage.Dosage, False, "fixed", False),
            ("fixedDuration", "fixedDuration", duration.Duration, False, "fixed", False),
            ("fixedExpression", "fixedExpression", expression.Expression, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("_fixedId", "_fixedId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False),
            ("fixedInstant", "fixedInstant", FHIRDate, False, "fixed", False),
            ("_fixedInstant", "_fixedInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("_fixedInteger", "_fixedInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("_fixedMarkdown", "_fixedMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedMoney", "fixedMoney", money.Money, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("_fixedOid", "_fixedOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedParameterDefinition", "fixedParameterDefinition", parameterdefinition.ParameterDefinition, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("_fixedPositiveInt", "_fixedPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", relatedartifact.RelatedArtifact, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("_fixedString", "_fixedString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedTime", "fixedTime", FHIRDate, False, "fixed", False),
            ("_fixedTime", "_fixedTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", triggerdefinition.TriggerDefinition, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("_fixedUnsignedInt", "_fixedUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("_fixedUri", "_fixedUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("_fixedUrl", "_fixedUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fixedUsageContext", "fixedUsageContext", usagecontext.UsageContext, False, "fixed", False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("_fixedUuid", "_fixedUuid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("_isModifier", "_isModifier",fhirprimitive.FHIRPrimitive, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("_isModifierReason", "_isModifierReason",fhirprimitive.FHIRPrimitive, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("_isSummary", "_isSummary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("label", "label", str, False, None, False),
            ("_label", "_label",fhirprimitive.FHIRPrimitive, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("_maxLength", "_maxLength",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueDate", "maxValueDate", FHIRDate, False, "maxValue", False),
            ("_maxValueDate", "_maxValueDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueDateTime", "maxValueDateTime", FHIRDate, False, "maxValue", False),
            ("_maxValueDateTime", "_maxValueDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("_maxValueDecimal", "_maxValueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueInstant", "maxValueInstant", FHIRDate, False, "maxValue", False),
            ("_maxValueInstant", "_maxValueInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("_maxValueInteger", "_maxValueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("_maxValuePositiveInt", "_maxValuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", FHIRDate, False, "maxValue", False),
            ("_maxValueTime", "_maxValueTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("_maxValueUnsignedInt", "_maxValueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("_meaningWhenMissing", "_meaningWhenMissing",fhirprimitive.FHIRPrimitive, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueDate", "minValueDate", FHIRDate, False, "minValue", False),
            ("_minValueDate", "_minValueDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueDateTime", "minValueDateTime", FHIRDate, False, "minValue", False),
            ("_minValueDateTime", "_minValueDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("_minValueDecimal", "_minValueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueInstant", "minValueInstant", FHIRDate, False, "minValue", False),
            ("_minValueInstant", "_minValueInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("_minValueInteger", "_minValueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("_minValuePositiveInt", "_minValuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False),
            ("minValueTime", "minValueTime", FHIRDate, False, "minValue", False),
            ("_minValueTime", "_minValueTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("_minValueUnsignedInt", "_minValueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("_mustSupport", "_mustSupport",fhirprimitive.FHIRPrimitive, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("_orderMeaning", "_orderMeaning",fhirprimitive.FHIRPrimitive, False, None, False),
            ("path", "path", str, False, None, True),
            ("_path", "_path",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False),
            ("patternAge", "patternAge", age.Age, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("_patternBase64Binary", "_patternBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("_patternBoolean", "_patternBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("_patternCanonical", "_patternCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("_patternCode", "_patternCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False),
            ("patternContactDetail", "patternContactDetail", contactdetail.ContactDetail, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False),
            ("patternContributor", "patternContributor", contributor.Contributor, False, "pattern", False),
            ("patternCount", "patternCount", count.Count, False, "pattern", False),
            ("patternDataRequirement", "patternDataRequirement", datarequirement.DataRequirement, False, "pattern", False),
            ("patternDate", "patternDate", FHIRDate, False, "pattern", False),
            ("_patternDate", "_patternDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternDateTime", "patternDateTime", FHIRDate, False, "pattern", False),
            ("_patternDateTime", "_patternDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("_patternDecimal", "_patternDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternDistance", "patternDistance", distance.Distance, False, "pattern", False),
            ("patternDosage", "patternDosage", dosage.Dosage, False, "pattern", False),
            ("patternDuration", "patternDuration", duration.Duration, False, "pattern", False),
            ("patternExpression", "patternExpression", expression.Expression, False, "pattern", False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("_patternId", "_patternId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False),
            ("patternInstant", "patternInstant", FHIRDate, False, "pattern", False),
            ("_patternInstant", "_patternInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("_patternInteger", "_patternInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("_patternMarkdown", "_patternMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternMoney", "patternMoney", money.Money, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("_patternOid", "_patternOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternParameterDefinition", "patternParameterDefinition", parameterdefinition.ParameterDefinition, False, "pattern", False),
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("_patternPositiveInt", "_patternPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False),
            ("patternRange", "patternRange", range.Range, False, "pattern", False),
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False),
            ("patternRelatedArtifact", "patternRelatedArtifact", relatedartifact.RelatedArtifact, False, "pattern", False),
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("_patternString", "_patternString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternTime", "patternTime", FHIRDate, False, "pattern", False),
            ("_patternTime", "_patternTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False),
            ("patternTriggerDefinition", "patternTriggerDefinition", triggerdefinition.TriggerDefinition, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("_patternUnsignedInt", "_patternUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("_patternUri", "_patternUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("_patternUrl", "_patternUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patternUsageContext", "patternUsageContext", usagecontext.UsageContext, False, "pattern", False),
            ("patternUuid", "patternUuid", str, False, "pattern", False),
            ("_patternUuid", "_patternUuid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("representation", "representation", str, True, None, False),
            ("_representation", "_representation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("_requirements", "_requirements",fhirprimitive.FHIRPrimitive, False, None, False),
            ("short", "short", str, False, None, False),
            ("_short", "_short",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False),
            ("_sliceIsConstraining", "_sliceIsConstraining",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("_sliceName", "_sliceName",fhirprimitive.FHIRPrimitive, False, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
        ])
        return js


from . import element

class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.
    
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """
    
    resource_type = "ElementDefinitionBase"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.max = None
        
        """ Max cardinality of the base element.
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.min = None
        
        """ Min cardinality of the base element.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.path = None
        
        """ Path that identifies the base element.
        Type `str`. """
        
        self._path = None
        
        """ extension for fhir primitive  path"""
        
        super(ElementDefinitionBase, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("max", "max", str, False, None, True),
            ("_max", "_max",fhirprimitive.FHIRPrimitive, False, None, False),
            ("min", "min", int, False, None, True),
            ("_min", "_min",fhirprimitive.FHIRPrimitive, False, None, False),
            ("path", "path", str, False, None, True),
            ("_path", "_path",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    
    resource_type = "ElementDefinitionBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Human explanation of the value set.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.strength = None
        
        """ required | extensible | preferred | example.
        Type `str`. """
        
        self._strength = None
        
        """ extension for fhir primitive  strength"""
        
        self.valueSet = None
        
        """ Source of value set.
        Type `str`. """
        
        self._valueSet = None
        
        """ extension for fhir primitive  valueSet"""
        
        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("_strength", "_strength",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("_valueSet", "_valueSet",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    resource_type = "ElementDefinitionConstraint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        
        """ FHIRPath expression of constraint.
        Type `str`. """
        
        self._expression = None
        
        """ extension for fhir primitive  expression"""
        
        self.human = None
        
        """ Human description of constraint.
        Type `str`. """
        
        self._human = None
        
        """ extension for fhir primitive  human"""
        
        self.key = None
        
        """ Target of 'condition' reference above.
        Type `str`. """
        
        self._key = None
        
        """ extension for fhir primitive  key"""
        
        self.requirements = None
        
        """ Why this constraint is necessary or appropriate.
        Type `str`. """
        
        self._requirements = None
        
        """ extension for fhir primitive  requirements"""
        
        self.severity = None
        
        """ error | warning.
        Type `str`. """
        
        self._severity = None
        
        """ extension for fhir primitive  severity"""
        
        self.source = None
        
        """ Reference to original source of constraint.
        Type `str`. """
        
        self._source = None
        
        """ extension for fhir primitive  source"""
        
        self.xpath = None
        
        """ XPath expression of constraint.
        Type `str`. """
        
        self._xpath = None
        
        """ extension for fhir primitive  xpath"""
        
        super(ElementDefinitionConstraint, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression",fhirprimitive.FHIRPrimitive, False, None, False),
            ("human", "human", str, False, None, True),
            ("_human", "_human",fhirprimitive.FHIRPrimitive, False, None, False),
            ("key", "key", str, False, None, True),
            ("_key", "_key",fhirprimitive.FHIRPrimitive, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("_requirements", "_requirements",fhirprimitive.FHIRPrimitive, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("_severity", "_severity",fhirprimitive.FHIRPrimitive, False, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source",fhirprimitive.FHIRPrimitive, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("_xpath", "_xpath",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).
    
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    
    resource_type = "ElementDefinitionExample"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.label = None
        
        """ Describes the purpose of this example.
        Type `str`. """
        
        self._label = None
        
        """ extension for fhir primitive  label"""
        
        self.valueAddress = None
        
        """ Value of Example (one of allowed types).
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        
        """ Value of Example (one of allowed types).
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        
        """ Value of Example (one of allowed types).
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ Value of Example (one of allowed types).
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueBase64Binary = None
        
        """ extension for fhir primitive  valueBase64Binary"""
        
        self.valueBoolean = None
        
        """ Value of Example (one of allowed types).
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCanonical = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueCanonical = None
        
        """ extension for fhir primitive  valueCanonical"""
        
        self.valueCode = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueCodeableConcept = None
        
        """ Value of Example (one of allowed types).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        
        """ Value of Example (one of allowed types).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        
        """ Value of Example (one of allowed types).
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        
        """ Value of Example (one of allowed types).
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        
        """ Value of Example (one of allowed types).
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        
        """ Value of Example (one of allowed types).
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        
        """ Value of Example (one of allowed types).
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueDate = None
        
        """ extension for fhir primitive  valueDate"""
        
        self.valueDateTime = None
        
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueDateTime = None
        
        """ extension for fhir primitive  valueDateTime"""
        
        self.valueDecimal = None
        
        """ Value of Example (one of allowed types).
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueDistance = None
        
        """ Value of Example (one of allowed types).
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        
        """ Value of Example (one of allowed types).
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        
        """ Value of Example (one of allowed types).
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        
        """ Value of Example (one of allowed types).
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        
        """ Value of Example (one of allowed types).
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueId = None
        
        """ extension for fhir primitive  valueId"""
        
        self.valueIdentifier = None
        
        """ Value of Example (one of allowed types).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueInstant = None
        
        """ extension for fhir primitive  valueInstant"""
        
        self.valueInteger = None
        
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueMarkdown = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueMarkdown = None
        
        """ extension for fhir primitive  valueMarkdown"""
        
        self.valueMoney = None
        
        """ Value of Example (one of allowed types).
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueOid = None
        
        """ extension for fhir primitive  valueOid"""
        
        self.valueParameterDefinition = None
        
        """ Value of Example (one of allowed types).
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        
        """ Value of Example (one of allowed types).
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self._valuePositiveInt = None
        
        """ extension for fhir primitive  valuePositiveInt"""
        
        self.valueQuantity = None
        
        """ Value of Example (one of allowed types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        
        """ Value of Example (one of allowed types).
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        
        """ Value of Example (one of allowed types).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Value of Example (one of allowed types).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        
        """ Value of Example (one of allowed types).
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        
        """ Value of Example (one of allowed types).
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        
        """ Value of Example (one of allowed types).
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._valueTime = None
        
        """ extension for fhir primitive  valueTime"""
        
        self.valueTiming = None
        
        """ Value of Example (one of allowed types).
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        
        """ Value of Example (one of allowed types).
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self._valueUnsignedInt = None
        
        """ extension for fhir primitive  valueUnsignedInt"""
        
        self.valueUri = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        self.valueUrl = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueUrl = None
        
        """ extension for fhir primitive  valueUrl"""
        
        self.valueUsageContext = None
        
        """ Value of Example (one of allowed types).
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self._valueUuid = None
        
        """ extension for fhir primitive  valueUuid"""
        
        super(ElementDefinitionExample, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
            ("_label", "_label",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("_valueCanonical", "_valueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("_valueDateTime", "_valueDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", FHIRDate, False, "value", True),
            ("_valueInstant", "_valueInstant",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("_valueMarkdown", "_valueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("_valueOid", "_valueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("_valuePositiveInt", "_valuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("_valueTime", "_valueTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("_valueUnsignedInt", "_valueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("_valueUrl", "_valueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("_valueUuid", "_valueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    resource_type = "ElementDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        
        """ Comments about the mapping or its use.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.identity = None
        
        """ Reference to mapping declaration.
        Type `str`. """
        
        self._identity = None
        
        """ extension for fhir primitive  identity"""
        
        self.language = None
        
        """ Computable language of mapping.
        Type `str`. """
        
        self._language = None
        
        """ extension for fhir primitive  language"""
        
        self.map = None
        
        """ Details of the mapping.
        Type `str`. """
        
        self._map = None
        
        """ extension for fhir primitive  map"""
        
        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("_identity", "_identity",fhirprimitive.FHIRPrimitive, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language",fhirprimitive.FHIRPrimitive, False, None, False),
            ("map", "map", str, False, None, True),
            ("_map", "_map",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.
    
    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    
    resource_type = "ElementDefinitionSlicing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Text description of how slicing works (or not).
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.discriminator = None
        
        """ Element values that are used to distinguish the slices.
        List of `ElementDefinitionSlicingDiscriminator` items (represented as `dict` in JSON). """
        
        self.ordered = None
        
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self._ordered = None
        
        """ extension for fhir primitive  ordered"""
        
        self.rules = None
        
        """ closed | open | openAtEnd.
        Type `str`. """
        
        self._rules = None
        
        """ extension for fhir primitive  rules"""
        
        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("_ordered", "_ordered",fhirprimitive.FHIRPrimitive, False, None, False),
            ("rules", "rules", str, False, None, True),
            ("_rules", "_rules",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.
    
    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    
    resource_type = "ElementDefinitionSlicingDiscriminator"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        
        """ Path to element value.
        Type `str`. """
        
        self._path = None
        
        """ extension for fhir primitive  path"""
        
        self.type = None
        
        """ value | exists | pattern | type | profile.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ElementDefinitionSlicingDiscriminator, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("_path", "_path",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    resource_type = "ElementDefinitionType"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.aggregation = None
        
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """
        
        self._aggregation = None
        
        """ extension for fhir primitive  aggregation"""
        
        self.code = None
        
        """ Data type or Resource (reference to definition).
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.profile = None
        
        """ Profiles (StructureDefinition or IG) - one must apply.
        List of `str` items. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.targetProfile = None
        
        """ Profile (StructureDefinition or IG) on the Reference/canonical
        target - one must apply.
        List of `str` items. """
        
        self._targetProfile = None
        
        """ extension for fhir primitive  targetProfile"""
        
        self.versioning = None
        
        """ either | independent | specific.
        Type `str`. """
        
        self._versioning = None
        
        """ extension for fhir primitive  versioning"""
        
        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True, None, False),
            ("_aggregation", "_aggregation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("_targetProfile", "_targetProfile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("versioning", "versioning", str, False, None, False),
            ("_versioning", "_versioning",fhirprimitive.FHIRPrimitive, False, None, False),
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
