#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/PractitionerRole) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class PractitionerRole(domainresource.DomainResource):
    """ Roles/organizations the practitioner is associated with.
    
    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    
    resource_type = "PractitionerRole"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        
        """ Whether this practitioner role record is in active use.
        Type `bool`. """
        
        self._active = None
        
        """ extension for fhir primitive  active"""
        
        self.availabilityExceptions = None
        
        """ Description of availability exceptions.
        Type `str`. """
        
        self._availabilityExceptions = None
        
        """ extension for fhir primitive  availabilityExceptions"""
        
        self.availableTime = None
        
        """ Times the Service Site is available.
        List of `PractitionerRoleAvailableTime` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Roles which this practitioner may perform.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        
        """ Technical endpoints providing access to services operated for the
        practitioner with this role.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.healthcareService = None
        
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifiers that are specific to a role/location.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.notAvailable = None
        
        """ Not available during this time due to provided reason.
        List of `PractitionerRoleNotAvailable` items (represented as `dict` in JSON). """
        
        self.organization = None
        
        """ Organization where the roles are available.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.practitioner = None
        
        """ Practitioner that is able to provide the defined services for the
        organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.specialty = None
        
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        
        """ Contact details that are specific to the role/location/service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(PractitionerRole, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("_availabilityExceptions", "_availabilityExceptions",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("practitioner", "practitioner", fhirreference.FHIRReference, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """
    
    resource_type = "PractitionerRoleAvailableTime"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        
        """ Always available? e.g. 24 hour service.
        Type `bool`. """
        
        self._allDay = None
        
        """ extension for fhir primitive  allDay"""
        
        self.availableEndTime = None
        
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._availableEndTime = None
        
        """ extension for fhir primitive  availableEndTime"""
        
        self.availableStartTime = None
        
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._availableStartTime = None
        
        """ extension for fhir primitive  availableStartTime"""
        
        self.daysOfWeek = None
        
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        self._daysOfWeek = None
        
        """ extension for fhir primitive  daysOfWeek"""
        
        super(PractitionerRoleAvailableTime, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("_allDay", "_allDay",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availableEndTime", "availableEndTime", FHIRDate, False, None, False),
            ("_availableEndTime", "_availableEndTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availableStartTime", "availableStartTime", FHIRDate, False, None, False),
            ("_availableStartTime", "_availableStartTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("_daysOfWeek", "_daysOfWeek",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """
    
    resource_type = "PractitionerRoleNotAvailable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.during = None
        
        """ Service not available from this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerRoleNotAvailable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

