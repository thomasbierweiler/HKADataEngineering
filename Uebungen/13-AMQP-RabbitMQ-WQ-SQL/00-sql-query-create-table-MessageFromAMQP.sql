USE [HKA_AMQP]
GO

/****** Object:  Table [dbo].[MessageFromAMQP]    Script Date: 14.10.2021 13:58:29 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[MessageFromAMQP](
	[timestamp] [datetime2](7) NULL,
	[message] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


