---
hide:
  - toc
---

# shared-commonSimpleTypes.xsd

- **前缀**: `s`
- **命名空间**: **`http://purl.oclc.org/ooxml/officeDocument/sharedTypes`**

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns="http://purl.oclc.org/ooxml/officeDocument/sharedTypes"
  targetNamespace="http://purl.oclc.org/ooxml/officeDocument/sharedTypes"
  elementFormDefault="qualified">
  
  <xsd:simpleType name="ST_Lang">
    <xsd:restriction base="xsd:string"/>
  </xsd:simpleType>
  <xsd:simpleType name="ST_HexColorRGB">
    <xsd:restriction base="xsd:hexBinary">
      <xsd:length value="3" fixed="true"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_Panose">
    <xsd:restriction base="xsd:hexBinary">
      <xsd:length value="10"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_CalendarType">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="gregorian"/>
      <xsd:enumeration value="gregorianUs"/>
      <xsd:enumeration value="gregorianMeFrench"/>
      <xsd:enumeration value="gregorianArabic"/>
      <xsd:enumeration value="hijri"/>
      <xsd:enumeration value="hebrew"/>
      <xsd:enumeration value="taiwan"/>
      <xsd:enumeration value="japan"/>
      <xsd:enumeration value="thai"/>
      <xsd:enumeration value="korea"/>
      <xsd:enumeration value="saka"/>
      <xsd:enumeration value="gregorianXlitEnglish"/>
      <xsd:enumeration value="gregorianXlitFrench"/>
      <xsd:enumeration value="none"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_Guid">
    <xsd:restriction base="xsd:token">
      <xsd:pattern value="\{[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}\}"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_OnOff">
    <xsd:union memberTypes="xsd:boolean"/>
  </xsd:simpleType>
  <xsd:simpleType name="ST_String">
    <xsd:restriction base="xsd:string"/>
  </xsd:simpleType>
  <xsd:simpleType name="ST_XmlName">
    <xsd:restriction base="xsd:NCName">
      <xsd:minLength value="1"/>
      <xsd:maxLength value="255"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_UnsignedDecimalNumber">
    <xsd:restriction base="xsd:unsignedLong"/>
  </xsd:simpleType>
  <xsd:simpleType name="ST_TwipsMeasure">
    <xsd:union memberTypes="ST_UnsignedDecimalNumber ST_PositiveUniversalMeasure"/>
  </xsd:simpleType>
  <xsd:simpleType name="ST_VerticalAlignRun">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="baseline"/>
      <xsd:enumeration value="superscript"/>
      <xsd:enumeration value="subscript"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_Xstring">
    <xsd:restriction base="xsd:string"/>
  </xsd:simpleType>
  <xsd:simpleType name="ST_XAlign">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="left"/>
      <xsd:enumeration value="center"/>
      <xsd:enumeration value="right"/>
      <xsd:enumeration value="inside"/>
      <xsd:enumeration value="outside"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_YAlign">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="inline"/>
      <xsd:enumeration value="top"/>
      <xsd:enumeration value="center"/>
      <xsd:enumeration value="bottom"/>
      <xsd:enumeration value="inside"/>
      <xsd:enumeration value="outside"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_ConformanceClass">
    <xsd:restriction base="xsd:string">
      <xsd:enumeration value="strict"/>
      <xsd:enumeration value="transitional"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_UniversalMeasure">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="-?[0-9]+(\.[0-9]+)?(mm|cm|in|pt|pc|pi)"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_PositiveUniversalMeasure">
    <xsd:restriction base="ST_UniversalMeasure">
      <xsd:pattern value="[0-9]+(\.[0-9]+)?(mm|cm|in|pt|pc|pi)"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_Percentage">
    <xsd:restriction base="xsd:string">
      <xsd:pattern value="-?[0-9]+(\.[0-9]+)?%"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_FixedPercentage">
    <xsd:restriction base="ST_Percentage">
      <xsd:pattern value="-?((100)|([0-9][0-9]?))(\.[0-9][0-9]?)?%"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_PositivePercentage">
    <xsd:restriction base="ST_Percentage">
      <xsd:pattern value="[0-9]+(\.[0-9]+)?%"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="ST_PositiveFixedPercentage">
    <xsd:restriction base="ST_Percentage">
      <xsd:pattern value="((100)|([0-9][0-9]?))(\.[0-9][0-9]?)?%"/>
    </xsd:restriction>
  </xsd:simpleType>
</xsd:schema>
```
