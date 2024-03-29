---
hide:
  - toc
---

# shared-customXmlDataProperties.xsd

- **前缀**: `ds`
- **命名空间**: **`http://purl.oclc.org/ooxml/officeDocument/customXml`**
- **相关命名空间**:
    - `s`: [**`http://purl.oclc.org/ooxml/officeDocument/sharedTypes`**](./shared-commonSimpleTypes.md)

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://purl.oclc.org/ooxml/officeDocument/customXml"
  xmlns:s="http://purl.oclc.org/ooxml/officeDocument/sharedTypes"
  targetNamespace="http://purl.oclc.org/ooxml/officeDocument/customXml"
  elementFormDefault="qualified" attributeFormDefault="qualified" blockDefault="#all">

  <xsd:import namespace="http://purl.oclc.org/ooxml/officeDocument/sharedTypes"
    schemaLocation="shared-commonSimpleTypes.xsd"/>
  <xsd:complexType name="CT_DatastoreSchemaRef">
    <xsd:attribute name="uri" type="xsd:string" use="required"/>
  </xsd:complexType>
  <xsd:complexType name="CT_DatastoreSchemaRefs">
    <xsd:sequence>
      <xsd:element name="schemaRef" type="CT_DatastoreSchemaRef" minOccurs="0" maxOccurs="unbounded"
      />
    </xsd:sequence>
  </xsd:complexType>
  <xsd:complexType name="CT_DatastoreItem">
    <xsd:sequence>
      <xsd:element name="schemaRefs" type="CT_DatastoreSchemaRefs" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="itemID" type="s:ST_Guid" use="required"/>
  </xsd:complexType>
  <xsd:element name="datastoreItem" type="CT_DatastoreItem"/>
</xsd:schema>
```
