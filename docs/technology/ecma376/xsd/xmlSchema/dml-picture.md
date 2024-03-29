---
hide:
  - toc
---

# dml-picture.xsd

- **前缀**: `pic`
- **命名空间**: **`http://purl.oclc.org/ooxml/drawingml/picture`**
- **相关命名空间**:
    - `a`: [**`http://purl.oclc.org/ooxml/drawingml/main`**](./dml-main.md)

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://purl.oclc.org/ooxml/drawingml/picture"
  xmlns:a="http://purl.oclc.org/ooxml/drawingml/main" elementFormDefault="qualified"
  targetNamespace="http://purl.oclc.org/ooxml/drawingml/picture">
  <xsd:import namespace="http://purl.oclc.org/ooxml/drawingml/main" schemaLocation="dml-main.xsd"/>
  <xsd:complexType name="CT_PictureNonVisual">
    <xsd:sequence>
      <xsd:element name="cNvPr" type="a:CT_NonVisualDrawingProps" minOccurs="1" maxOccurs="1"/>
      <xsd:element name="cNvPicPr" type="a:CT_NonVisualPictureProperties" minOccurs="1"
        maxOccurs="1"/>
    </xsd:sequence>
  </xsd:complexType>
  <xsd:complexType name="CT_Picture">
    <xsd:sequence minOccurs="1" maxOccurs="1">
      <xsd:element name="nvPicPr" type="CT_PictureNonVisual" minOccurs="1" maxOccurs="1"/>
      <xsd:element name="blipFill" type="a:CT_BlipFillProperties" minOccurs="1" maxOccurs="1"/>
      <xsd:element name="spPr" type="a:CT_ShapeProperties" minOccurs="1" maxOccurs="1"/>
    </xsd:sequence>
  </xsd:complexType>
  <xsd:element name="pic" type="CT_Picture"/>
</xsd:schema>
```
