#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.
    
    A kind of specimen with associated set of requirements.
    """
    
    resource_type = "SpecimenDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        
        """ Specimen collection procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier of a kind of specimen.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientPreparation = None
        
        """ Patient preparation for collection.
        Type `str`. """
        
        self._patientPreparation = None
        
        """ extension for fhir primitive  patientPreparation"""
        
        self.timeAspect = None
        
        """ Time aspect for collection.
        Type `str`. """
        
        self._timeAspect = None
        
        """ extension for fhir primitive  timeAspect"""
        
        self.typeCollected = None
        
        """ Kind of material to collect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.typeTested = None
        
        """ Specimen in container intended for testing by lab.
        List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON). """
        
        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patientPreparation", "patientPreparation", str, False, None, False),
            ("_patientPreparation", "_patientPreparation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("_timeAspect", "_timeAspect",fhirprimitive.FHIRPrimitive, False, None, False),
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False),
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False),
        ])
        return js


from . import backboneelement

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.
    
    Specimen conditioned in a container as expected by the testing laboratory.
    """
    
    resource_type = "SpecimenDefinitionTypeTested"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.container = None
        
        """ The specimen's container.
        Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON). """
        
        self.handling = None
        
        """ Specimen handling before testing.
        List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON). """
        
        self.isDerived = None
        
        """ Primary or secondary specimen.
        Type `bool`. """
        
        self._isDerived = None
        
        """ extension for fhir primitive  isDerived"""
        
        self.preference = None
        
        """ preferred | alternate.
        Type `str`. """
        
        self._preference = None
        
        """ extension for fhir primitive  preference"""
        
        self.rejectionCriterion = None
        
        """ Rejection criterion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requirement = None
        
        """ Specimen requirements.
        Type `str`. """
        
        self._requirement = None
        
        """ extension for fhir primitive  requirement"""
        
        self.retentionTime = None
        
        """ Specimen retention time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of intended specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTested, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False),
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False),
            ("isDerived", "isDerived", bool, False, None, True),
            ("_isDerived", "_isDerived",fhirprimitive.FHIRPrimitive, False, None, False),
            ("preference", "preference", str, False, None, True),
            ("_preference", "_preference",fhirprimitive.FHIRPrimitive, False, None, False),
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("_requirement", "_requirement",fhirprimitive.FHIRPrimitive, False, None, False),
            ("retentionTime", "retentionTime", duration.Duration, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        
        """ Additive associated with container.
        List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON). """
        
        self.cap = None
        
        """ Color of container cap.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.capacity = None
        
        """ Container capacity.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Container description.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.material = None
        
        """ Container material.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.minimumVolume = None
        
        """ Minimum volume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.preparation = None
        
        """ Specimen container preparation.
        Type `str`. """
        
        self._preparation = None
        
        """ extension for fhir primitive  preparation"""
        
        self.type = None
        
        """ Kind of container associated with the kind of specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False),
            ("cap", "cap", codeableconcept.CodeableConcept, False, None, False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("minimumVolume", "minimumVolume", quantity.Quantity, False, None, False),
            ("preparation", "preparation", str, False, None, False),
            ("_preparation", "_preparation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.
    
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainerAdditive"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainerAdditive, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True),
        ])
        return js


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.
    
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedHandling"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction = None
        
        """ Preservation instruction.
        Type `str`. """
        
        self._instruction = None
        
        """ extension for fhir primitive  instruction"""
        
        self.maxDuration = None
        
        """ Maximum preservation time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.temperatureQualifier = None
        
        """ Temperature qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.temperatureRange = None
        
        """ Temperature range.
        Type `Range` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedHandling, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("_instruction", "_instruction",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxDuration", "maxDuration", duration.Duration, False, None, False),
            ("temperatureQualifier", "temperatureQualifier", codeableconcept.CodeableConcept, False, None, False),
            ("temperatureRange", "temperatureRange", range.Range, False, None, False),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import fhirprimitive

