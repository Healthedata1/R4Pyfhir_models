#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Patient) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.
    
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    
    resource_type = "Patient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        
        """ Whether this patient's record is in active use.
        Type `bool`. """
        
        self._active = None
        
        """ extension for fhir primitive  active"""
        
        self.address = None
        
        """ An address for the individual.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        
        """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._birthDate = None
        
        """ extension for fhir primitive  birthDate"""
        
        self.communication = None
        
        """ A language which may be used to communicate with the patient about
        his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """
        
        self.contact = None
        
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """
        
        self.deceasedBoolean = None
        
        """ Indicates if the individual is deceased or not.
        Type `bool`. """
        
        self._deceasedBoolean = None
        
        """ extension for fhir primitive  deceasedBoolean"""
        
        self.deceasedDateTime = None
        
        """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._deceasedDateTime = None
        
        """ extension for fhir primitive  deceasedDateTime"""
        
        self.gender = None
        
        """ male | female | other | unknown.
        Type `str`. """
        
        self._gender = None
        
        """ extension for fhir primitive  gender"""
        
        self.generalPractitioner = None
        
        """ Patient's nominated primary care provider.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.link = None
        
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.maritalStatus = None
        
        """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleBirthBoolean = None
        
        """ Whether patient is part of a multiple birth.
        Type `bool`. """
        
        self._multipleBirthBoolean = None
        
        """ extension for fhir primitive  multipleBirthBoolean"""
        
        self.multipleBirthInteger = None
        
        """ Whether patient is part of a multiple birth.
        Type `int`. """
        
        self._multipleBirthInteger = None
        
        """ extension for fhir primitive  multipleBirthInteger"""
        
        self.name = None
        
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.photo = None
        
        """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.telecom = None
        
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Patient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active",fhirprimitive.FHIRPrimitive, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("_birthDate", "_birthDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("_deceasedBoolean", "_deceasedBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("deceasedDateTime", "deceasedDateTime", FHIRDate, False, "deceased", False),
            ("_deceasedDateTime", "_deceasedDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender",fhirprimitive.FHIRPrimitive, False, None, False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PatientLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("_multipleBirthBoolean", "_multipleBirthBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("_multipleBirthInteger", "_multipleBirthInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """
    
    resource_type = "PatientCommunication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        
        """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.preferred = None
        
        """ Language preference indicator.
        Type `bool`. """
        
        self._preferred = None
        
        """ extension for fhir primitive  preferred"""
        
        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
            ("_preferred", "_preferred",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    
    resource_type = "PatientContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        
        """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        
        """ male | female | other | unknown.
        Type `str`. """
        
        self._gender = None
        
        """ extension for fhir primitive  gender"""
        
        self.name = None
        
        """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.organization = None
        
        """ Organization that is associated with the contact.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        
        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """
        
        self.relationship = None
        
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.
    
    Link to another patient resource that concerns the same actual patient.
    """
    
    resource_type = "PatientLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.other = None
        
        """ The other patient or related person resource that the link refers
        to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ replaced-by | replaces | refer | seealso.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier
from . import period
from . import fhirprimitive

