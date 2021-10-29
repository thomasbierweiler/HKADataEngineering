USE [MQTT-Beschleunigung]
GO

/****** Object:  Table [dbo].[Messwerte_Rohformat]    Script Date: 21.10.2021 20:01:44 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Messwerte_Rohformat](
	[StartMessung] [datetime2](7) NULL,
	[EmpfangNachricht] [datetime2](7) NULL,
	[Rohsignal] [varbinary](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

USE [MQTT-Beschleunigung]
GO

/****** Object:  Table [dbo].[Messwerte_Einzeln]    Script Date: 21.10.2021 20:01:38 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Messwerte_Einzeln](
	[StartMessung] [datetime2](7) NULL,
	[EmpfangNachricht] [datetime2](7) NULL,
	[Messwert] [smallint] NULL,
	[ZeitstempelMesswertErzeugung] [datetime2](7) NULL,
	[IdentifierDesPakets] [bigint] NULL
) ON [PRIMARY]
GO


