# !/usr/bin/env python3
# coding: utf-8 -*-
#
# Author: pipiche38
#


import struct
from Modules.tools import retreive_cmd_payload_from_8002
from Zigbee.encoder_tools import encapsulate_plugin_frame, decode_endian_data
from Modules.zigateConsts import ADDRESS_MODE, SIZE_DATA_TYPE


def zcl_decoders(self, SrcNwkId, SrcEndPoint, ClusterId, Payload, frame):

    GlobalCommand, Sqn, ManufacturerCode, Command, Data = retreive_cmd_payload_from_8002(Payload)


    if GlobalCommand:
        self.log.logging("zclDecoder", "Debug", "decode8002_and_process Sqn: %s/%s ManufCode: %s Command: %s Data: %s " % (int(Sqn, 16), Sqn, ManufacturerCode, Command, Data))
        if Command == "00":  # Read Attribute
            return buildframe_read_attribute_request(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Data)

        if Command == "01":  # Read Attribute response
            return buildframe_read_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data)

        if Command == "02":  # Write Attributes
            return buildframe_write_attribute_request(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Data)

        if Command == "04":  # Write Attribute response
            return buildframe_write_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data)

        if Command == "06":  # Configure Reporting
            return frame

        if Command == "07":  # Configure Reporting Response
            return buildframe_configure_reporting_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data)

        if Command == "0a":  # Report attributes
            return buildframe_report_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data)

        if Command == "0b":  #
            return frame

        if Command == "0d":  # Discover Attributes Response
            return buildframe_discover_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data)

    else: # Cluster Commands
        if ClusterId == "0006":
            # Remote report
            return buildframe_80x5_message(self, "8095", frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Command, Data)
        
        if ClusterId == "0008":
            # Remote report
            return buildframe_80x5_message(self, "8085", frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Command, Data)
        
        if ClusterId == "0019":
            # OTA Upgrade
            OTA_UPGRADE_COMMAND = {
                "00": "Image Notify",
                "01": "Query Next Image Request",
                "02": "Query Next Image response",
                "03": "Image Block Request",  # 8501
                "04": "Image Page request",
                "05": "Image Block Response",
                "06": "Upgrade End Request",  # 8503
                "07": "Upgrade End response",
                "08": "Query Device Specific File Request",
                "09": "Query Device Specific File response"
            }        
            if Command in OTA_UPGRADE_COMMAND:
                self.log.logging(
                    "zclDecoder",
                    "Log",
                    "zcl_decoders OTA Upgrade Command %s/%s data: %s" %(
                        Command, OTA_UPGRADE_COMMAND[ Command ], Data))
                return frame
    
        
        if ClusterId == "0500" and Command == "00":
            # Zone Enroll Response
            return buildframe_0400_cmd(self, "0400", frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Command, Data)

    self.log.logging(
        "zclDecoder",
        "Log",
        "zcl_decoders Unknown Command: %s NwkId: %s Ep: %s Cluster: %s Payload: %s - GlobalCommand: %s, Sqn: %s, ManufacturerCode: %s"
        % (
            Command,
            SrcNwkId,
            SrcEndPoint,
            ClusterId,
            Data,
            GlobalCommand,
            Sqn,
            ManufacturerCode,
        ),
    )

    return frame


def buildframe_discover_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data):

    self.log.logging("zclDecoder", "Debug", "buildframe_discover_attribute_response - Data: %s" % Data)
    discovery_complete = Data[:2]
    if discovery_complete == "01":
        Attribute_type = "00"
        Attribute = "0000"
    else:
        # It is assumed that only one attribute at a time is requested (this is not the standard)
        idx = 2
        Attribute_type = Data[idx : idx + 2]
        idx += 2
        Attribute = "%04x" % struct.unpack("H", struct.pack(">H", int(Data[idx : idx + 4], 16)))[0]
        idx += 4

    buildPayload = discovery_complete + Attribute_type + Attribute + SrcNwkId + SrcEndPoint + ClusterId
    return encapsulate_plugin_frame("8140", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


def buildframe_read_attribute_request(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_read_attribute_request - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))
    if len(Data) % 4 != 0:
        self.log.logging("zclDecoder", "Debug", "Most Likely Livolo Frame : %s (%s)" % (Data, len(Data)))
        return frame

    ManufSpec = "00"
    ManufCode = "0000"
    if ManufacturerCode:
        ManufSpec = "01"
        ManufCode = ManufacturerCode

    buildPayload = Sqn + SrcNwkId + SrcEndPoint + "01" + ClusterId + "01" + ManufSpec + ManufCode
    idx = nbAttribute = 0
    payloadOfAttributes = ""
    while idx < len(Data):
        nbAttribute += 1
        Attribute = "%04x" % struct.unpack("H", struct.pack(">H", int(Data[idx : idx + 4], 16)))[0]
        idx += 4
        payloadOfAttributes += Attribute

    buildPayload += "%02x" % (nbAttribute) + payloadOfAttributes
    return encapsulate_plugin_frame("0100", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


def buildframe_write_attribute_request(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_write_attribute_request - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))

    ManufSpec = "00"
    ManufCode = "0000"
    if ManufacturerCode:
        ManufSpec = "01"
        ManufCode = ManufacturerCode

    buildPayload = Sqn + SrcNwkId + SrcEndPoint + "01" + ClusterId + "01" + ManufSpec + ManufCode
    idx = nbAttribute = 0
    payloadOfAttributes = ""
    while idx < len(Data):
        nbAttribute += 1
        Attribute = "%04x" % struct.unpack("H", struct.pack(">H", int(Data[idx : idx + 4], 16)))[0]
        idx += 4

        DType = Data[idx : idx + 2]
        idx += 2
        if DType in SIZE_DATA_TYPE:
            size = SIZE_DATA_TYPE[DType] * 2
        elif DType in ("48", "4c"):
            nbElement = Data[idx + 2 : idx + 4] + Data[idx : idx + 2]
            idx += 4
            # Today found for attribute 0xff02 Xiaomi, just take all data
            size = len(Data) - idx

        elif DType in ("41", "42"):  # ZigBee_OctedString = 0x41, ZigBee_CharacterString = 0x42
            size = int(Data[idx : idx + 2], 16) * 2
            idx += 2
        else:
            self.log.logging("zclDecoder", "Error", "buildframe_write_attribute_request - Unknown DataType size: >%s< vs. %s " % (DType, str(SIZE_DATA_TYPE)))
            self.log.logging("zclDecoder", "Error", "buildframe_write_attribute_request - ClusterId: %s Attribute: %s Data: %s" % (ClusterId, Attribute, Data))
            return frame

        data = Data[idx : idx + size]
        idx += size
        value = decode_endian_data(data, DType)
        lenData = "%04x" % (size // 2)
        payloadOfAttributes += Attribute + DType + lenData + value

    buildPayload += "%02x" % (nbAttribute) + payloadOfAttributes
    return encapsulate_plugin_frame("0110", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


def buildframe_write_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_write_attribute_response - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))

    # This is based on assumption that we only Write 1 attribute at a time
    buildPayload = Sqn + SrcNwkId + SrcEndPoint + ClusterId + "0000" + Data
    return encapsulate_plugin_frame("8110", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


def buildframe_read_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_read_attribute_response - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))

    nbAttribute = 0
    idx = 0
    buildPayload = Sqn + SrcNwkId + SrcEndPoint + ClusterId
    while idx < len(Data):
        nbAttribute += 1
        Attribute = "%04x" % struct.unpack("H", struct.pack(">H", int(Data[idx : idx + 4], 16)))[0]
        idx += 4
        Status = Data[idx : idx + 2]
        idx += 2
        if Status == "00":
            DType = Data[idx : idx + 2]
            idx += 2
            if DType in SIZE_DATA_TYPE:
                size = SIZE_DATA_TYPE[DType] * 2
                data = Data[idx : idx + size]
                idx += size
                value = decode_endian_data(data, DType)
                lenData = "%04x" % (size // 2)

                
            elif DType in ("48", "4c"):
                nbElement = Data[idx + 2 : idx + 4] + Data[idx : idx + 2]
                idx += 4
                # Today found for attribute 0xff02 Xiaomi, just take all data
                size = len(Data) - idx
                data = Data[idx : idx + size]
                idx += size
                value = decode_endian_data(data, DType)
                lenData = "%04x" % (size // 2)


            elif DType in ("41", "42"):  # ZigBee_OctedString = 0x41, ZigBee_CharacterString = 0x42
                size = int(Data[idx : idx + 2], 16) * 2
                idx += 2
                data = Data[idx : idx + size]
                idx += size
                value = decode_endian_data(data, DType, size)
                lenData = "%04x" % (size // 2)

            else:
                self.log.logging("zclDecoder", "Error", "buildframe_read_attribute_response - Unknown DataType size: >%s< vs. %s " % (DType, str(SIZE_DATA_TYPE)))
                self.log.logging("zclDecoder", "Error", "buildframe_read_attribute_response - ClusterId: %s Attribute: %s Data: %s" % (ClusterId, Attribute, Data))
                return frame

            buildPayload += Attribute + Status + DType + lenData + value
        else:
            # Status != 0x00
            buildPayload += Attribute + Status

    return encapsulate_plugin_frame("8100", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


def buildframe_report_attribute_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_report_attribute_response - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))

    buildPayload = Sqn + SrcNwkId + SrcEndPoint + ClusterId
    nbAttribute = 0
    idx = 0
    while idx < len(Data):
        nbAttribute += 1
        Attribute = "%04x" % struct.unpack("H", struct.pack(">H", int(Data[idx : idx + 4], 16)))[0]
        idx += 4
        DType = Data[idx : idx + 2]
        idx += 2
        if DType in SIZE_DATA_TYPE:
            size = SIZE_DATA_TYPE[DType] * 2

        elif DType in ("48", "4c"):
            # Today found for attribute 0xff02 Xiaomi, just take all data
            nbElement = Data[idx + 2 : idx + 4] + Data[idx : idx + 2]
            idx += 4
            size = len(Data) - idx

        elif DType in ("41", "42"):  # ZigBee_OctedString = 0x41, ZigBee_CharacterString = 0x42
            size = int(Data[idx : idx + 2], 16) * 2
            idx += 2

        elif DType == "00":
            self.log.logging(
                "zclDecoder", "Error", "buildframe_report_attribute_response %s/%s Cluster: %s nbAttribute: %s Attribute: %s DType: %s idx: %s frame: %s" % (SrcNwkId, SrcEndPoint, ClusterId, nbAttribute, Attribute, DType, idx, frame)
            )
            return frame

        else:
            self.log.logging("zclDecoder", "Error", "buildframe_report_attribute_response - Unknown DataType size: >%s< vs. %s " % (DType, str(SIZE_DATA_TYPE)))
            self.log.logging("zclDecoder", "Error", "buildframe_report_attribute_response - NwkId: %s ClusterId: %s Attribute: %s Frame: %s" % (SrcNwkId, ClusterId, Attribute, frame))
            return frame

        data = Data[idx : idx + size]
        idx += size
        value = decode_endian_data(data, DType)
        lenData = "%04x" % (size // 2)
        buildPayload += Attribute + "00" + DType + lenData + value

    return encapsulate_plugin_frame("8102", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


def buildframe_configure_reporting_response(self, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_configure_reporting_response - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))

    if len(Data) == 2:
        nbAttribute = 1
        buildPayload = Sqn + SrcNwkId + SrcEndPoint + ClusterId + Data
    else:
        idx = 0
        nbAttribute = 0
        buildPayload = Sqn + SrcNwkId + SrcEndPoint + ClusterId
        while idx < len(Data):
            nbAttribute += 1
            Status = Data[idx : idx + 2]
            idx += 2
            Direction = Data[idx : idx + 2]
            idx += 2
            Attribute = "%04x" % struct.unpack("H", struct.pack(">H", int(Data[idx : idx + 4], 16)))[0]
            idx += 4
            buildPayload += Attribute + Status
        return frame

    return encapsulate_plugin_frame("8120", buildPayload, frame[len(frame) - 4 : len(frame) - 2])


## Cluster Specific commands
# Cluster 0x0006


def buildframe_80x5_message(self, MsgType, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Command, Data):
    # sourcery skip: assign-if-exp
    # handle_message Sender: 0x0EC8 frame for plugin: 0180020011ff00010400060101020ec8020000112401b103

    self.log.logging("zclDecoder", "Debug", "======> Building %s message : Cluster: %s Command: >%s< Data: >%s< (Frame: %s)" % (MsgType, ClusterId, Command, Data, frame))

    # It looks like the ZiGate firmware was adding _unknown (which is not part of the norm)
    unknown_ = Data[:2] if len(Data) >= 2 else "00"
    buildPayload = Sqn + SrcEndPoint + ClusterId + unknown_ + SrcNwkId + Command + Data[2:]

    return encapsulate_plugin_frame(MsgType, buildPayload, frame[len(frame) - 4 : len(frame) - 2])

## Cluster: 0x0019

## Cluster 0x0500
# Cmd : 0x00 Zone Enroll Response  -> 0400
#     : 0x01 Initiate Normal Operation Mode
#     : 0x02 Initiate Test mode

def buildframe_0400_cmd(self, MsgType, frame, Sqn, SrcNwkId, SrcEndPoint, ClusterId, ManufacturerCode, Command, Data):
    self.log.logging("zclDecoder", "Debug", "buildframe_configure_reporting_response - %s %s %s Data: %s" % (SrcNwkId, SrcEndPoint, ClusterId, Data))

    # Zone Enroll Response
    enroll_response_code = Data[:2]
    zone_id = Data[2:4]
    buildPayload = Sqn + SrcNwkId + SrcEndPoint + enroll_response_code + zone_id
    return encapsulate_plugin_frame( MsgType, buildPayload, frame[len(frame) - 4 : len(frame) - 2])
        

