#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Person) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class Person(domainresource.DomainResource):
    """ A generic person record.
    
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    
    resource_type = "Person"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        
        """ This person's record is in active use.
        Type `bool`. """
        
        self._active = None
        
        """ extension for fhir primitive  active"""
        
        self.address = None
        
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._birthDate = None
        
        """ extension for fhir primitive  birthDate"""
        
        self.gender = None
        
        """ male | female | other | unknown.
        Type `str`. """
        
        self._gender = None
        
        """ extension for fhir primitive  gender"""
        
        self.identifier = None
        
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.link = None
        
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name = None
        
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.photo = None
        
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.telecom = None
        
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Person, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active",fhirprimitive.FHIRPrimitive, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("_birthDate", "_birthDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PersonLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    
    resource_type = "PersonLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assurance = None
        
        """ level1 | level2 | level3 | level4.
        Type `str`. """
        
        self._assurance = None
        
        """ extension for fhir primitive  assurance"""
        
        self.target = None
        
        """ The resource to which this actual person is associated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("assurance", "assurance", str, False, None, False),
            ("_assurance", "_assurance",fhirprimitive.FHIRPrimitive, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import address
from . import attachment
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier
from . import fhirprimitive

