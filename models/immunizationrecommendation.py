#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    
    resource_type = "ImmunizationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        
        """ Who is responsible for protocol.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date recommendation(s) created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._date = None
        
        """ extension for fhir primitive  date"""
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        
        """ Who this profile is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recommendation = None
        
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, True),
            ("_date", "_date",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """
    
    resource_type = "ImmunizationRecommendationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contraindicatedVaccineCode = None
        
        """ Vaccine which is contraindicated to fulfill the recommendation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateCriterion = None
        
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Protocol details.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.doseNumberPositiveInt = None
        
        """ Recommended dose number within series.
        Type `int`. """
        
        self._doseNumberPositiveInt = None
        
        """ extension for fhir primitive  doseNumberPositiveInt"""
        
        self.doseNumberString = None
        
        """ Recommended dose number within series.
        Type `str`. """
        
        self._doseNumberString = None
        
        """ extension for fhir primitive  doseNumberString"""
        
        self.forecastReason = None
        
        """ Vaccine administration status reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.forecastStatus = None
        
        """ Vaccine recommendation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.series = None
        
        """ Name of vaccination series.
        Type `str`. """
        
        self._series = None
        
        """ extension for fhir primitive  series"""
        
        self.seriesDosesPositiveInt = None
        
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self._seriesDosesPositiveInt = None
        
        """ extension for fhir primitive  seriesDosesPositiveInt"""
        
        self.seriesDosesString = None
        
        """ Recommended number of doses for immunity.
        Type `str`. """
        
        self._seriesDosesString = None
        
        """ extension for fhir primitive  seriesDosesString"""
        
        self.supportingImmunization = None
        
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingPatientInformation = None
        
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.targetDisease = None
        
        """ Disease to be immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        
        """ Vaccine  or vaccine group recommendation applies to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("_doseNumberPositiveInt", "_doseNumberPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("_doseNumberString", "_doseNumberString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, True, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True),
            ("series", "series", str, False, None, False),
            ("_series", "_series",fhirprimitive.FHIRPrimitive, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("_seriesDosesPositiveInt", "_seriesDosesPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("_seriesDosesString", "_seriesDosesString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    
    resource_type = "ImmunizationRecommendationRecommendationDateCriterion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", FHIRDate, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import fhirprimitive

