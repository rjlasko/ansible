<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:strip-space elements="*" />
	<xsl:output encoding="UTF-8" indent="yes" omit-xml-declaration="yes" />

	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()" />
		</xsl:copy>
	</xsl:template>

	<xsl:template match="/domain[count(iothreads) = 0]">
		<xsl:copy>
			<xsl:apply-templates select="@*"/>
			<iothreads>3</iothreads>
			<xsl:apply-templates select="node()"/>
		</xsl:copy>
	</xsl:template>

	<xsl:template match="/domain/iothreads">
		<iothreads>4</iothreads>
	</xsl:template>

</xsl:stylesheet>
