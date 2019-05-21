#
# ** HEADER BEGIN **
#
# ** File: elam_defender_parser.py
#
# ** Author: Timo Schmid, Aleksandar Milenkoski (amilenkoski@ernw.de)
#
# ** Usage: pyton elam_defender_parser.py [database]
# [database]: a binary file containing the database of the ELAM driver
#
# ** Test environment: Windows 10, 64 bit, LTSB, build 1607
#
# ** Description: This script parses the malware database of the Microsoft Defender ELAM driver. It prints out: 
#      (i)   the signature and hash of the database
#      (ii)  information on each entry in the database:
#              the image category;
#              type of data stored (e.g., hash, issuer name);
#              data used for driver integrity verification (e.g., hash); and 
#              comments (typically filenames).
#    
#
# ** License:
#  elam_defender_parser.py
#  Copyright (C) 2017  Timo Schmid, Aleksandar Milenkoski
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ** HEADER END **
#

#
# ** SCRIPT BEGIN **
#

import argparse
import struct
from collections import namedtuple
import enum


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Util.number import bytes_to_long, long_to_bytes

from helperlib import print_hexII, print_hexdump, hexdump


class Item(namedtuple('Item', ['type', 'trust_code', 'data', 'comment'])):
    def __str__(self):
        l = [
            'DB entry:',
            f'\tType: {self.type!r}',
            f'\tImage category: {self.trust_code!r}',
            f'\tData:\n\t' + '\n\t'.join(hexdump(self.data, header=True)),
            f'\tComment: {self.comment}',
        ]
        return '\n'.join(l)


class EntryType(enum.IntEnum):
    THUMBPRINT_HASH = 1
    CERTIFICATE_PUBLISHER = 1
    ISSUER_NAME = 1
    IMAGE_HASH = 4
    VERSION_INFO = 7


class TrustLevel(enum.IntEnum):
    KnownGoodImage = 0
    KnownBadImage = 1
    UnknownImage_2 = 2
    UnknownImage = 3
    KnownBadImageBootCritical = 4


PUBLIC_EXPONENT = 0x010001

MODULUS = int.from_bytes(struct.pack("256B", *[
    0xb3, 0x95, 0xde, 0x5b, 0xc2, 0xe1, 0x89, 0xf7, 0x56, 0xc2, 0x20,
    0xbf, 0x27, 0xd2, 0x88, 0x1a, 0x0a, 0xac, 0xdb, 0xc7, 0x19, 0x36,
    0x7b, 0xce, 0x37, 0x83, 0xd1, 0xec, 0x42, 0xd3, 0xab, 0x30, 0x54,
    0xa5, 0x51, 0x11, 0xd8, 0xcc, 0xec, 0x80, 0xab, 0x89, 0x5a, 0xae,
    0x18, 0x71, 0x11, 0x7c, 0x85, 0x1a, 0x1a, 0x53, 0x54, 0x46, 0x3e,
    0x55, 0x5c, 0x43, 0x5d, 0x4b, 0x9f, 0xc7, 0x54, 0x57, 0x75, 0xc5,
    0x02, 0xe2, 0x63, 0xa9, 0x94, 0x56, 0xa7, 0x3b, 0xe0, 0xc3, 0xed,
    0x5f, 0x66, 0x9d, 0x60, 0x78, 0x1e, 0xac, 0x92, 0x3d, 0x48, 0xe9,
    0x51, 0x5d, 0x79, 0x2a, 0x22, 0x9a, 0x9e, 0xd3, 0xbc, 0x15, 0xbe,
    0x7a, 0x4e, 0x97, 0xe8, 0x1f, 0x9c, 0x80, 0xf5, 0xfb, 0x94, 0x0b,
    0x5f, 0xb7, 0x6f, 0x0d, 0x57, 0xa0, 0x09, 0x55, 0x68, 0x78, 0xf3,
    0x5d, 0x7b, 0x9a, 0x9b, 0x08, 0xa3, 0xa6, 0x41, 0x18, 0xf0, 0x17,
    0x11, 0x89, 0x9b, 0x71, 0x73, 0x27, 0xa2, 0x55, 0x51, 0xc0, 0xee,
    0xa5, 0x70, 0x6f, 0xb8, 0x40, 0x2a, 0x85, 0xe9, 0x91, 0x20, 0x4b,
    0x0c, 0xd2, 0x29, 0xa2, 0x01, 0x36, 0x96, 0x1c, 0xbb, 0xd5, 0xef,
    0x95, 0x68, 0x43, 0xfb, 0x77, 0x42, 0x88, 0x1a, 0xae, 0x60, 0x14,
    0xfe, 0x0b, 0x0d, 0xd3, 0x28, 0x04, 0x98, 0x15, 0x71, 0x3e, 0xba,
    0xb3, 0x80, 0x65, 0x6d, 0x2b, 0x7f, 0x30, 0xca, 0xf2, 0x6c, 0xa6,
    0x47, 0xd3, 0x3c, 0x57, 0x50, 0x0d, 0xb3, 0xbb, 0xed, 0x6d, 0x75,
    0xf2, 0x0f, 0x26, 0x29, 0xf7, 0xc6, 0xe4, 0x20, 0x5e, 0xaf, 0x87,
    0xf1, 0x8b, 0x8e, 0x57, 0x99, 0x00, 0xf3, 0x84, 0xe5, 0x25, 0x10,
    0x05, 0x2c, 0xeb, 0x77, 0xa3, 0xdb, 0xbd, 0x7e, 0xd4, 0xb5, 0x60,
    0xb6, 0x6a, 0xa0, 0x99, 0x25, 0x59, 0x2f, 0x10, 0x69, 0xf4, 0x62,
    0xe1, 0x8c, 0x2b]), 'big')


MODULUS = int.from_bytes(
    bytes.fromhex('b395de5bc2e189f756c220bf27d2881a0aacdbc719367bce3783d1ec42d3ab3054a55111d8ccec80ab895aae1871117c851a1a5354463e555c435d4b9fc7545775c502e263a99456a73be0c3ed5f669d60781eac923d48e9515d792a229a9ed3bc15be7a4e97e81f9c80f5fb940b5fb76f0d57a009556878f35d7b9a9b08a3a64118f01711899b717327a25551c0eea5706fb8402a85e991204b0cd229a20136961cbbd5ef956843fb7742881aae6014fe0b0dd328049815713ebab380656d2b7f30caf26ca647d33c57500db3bbed6d75f20f2629f7c6e4205eaf87f18b8e579900f384e52510052ceb77a3dbbd7ed4b560b66aa09925592f1069f462e18c2b'),
    'big')


PUBLIC_KEY = RSA.construct((MODULUS, PUBLIC_EXPONENT))


def parse(fp):
    tag = fp.read(1)[0]
    size = struct.unpack('<I', fp.read(3) + b'\0')[0]
    return tag, fp.read(size)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('Database', type=argparse.FileType('rb'))

    args = parser.parse_args(args=argv)
    fp = args.Database
    while True:
        try:
            tag, data = parse(fp)
        
            if tag == 0xA9:
                assert len(data) >= 4
                offset = struct.unpack_from('<I', data)[0] + 4
                assert offset < len(data)
                some_type = struct.unpack_from('<B', data[offset:])[0]
                if some_type == 9:
                    data_type, trust_code = struct.unpack_from('<BB', data[4:])
                    entry_data = data[6:offset]
                    item = Item(EntryType(data_type), TrustLevel(trust_code),
                                entry_data, data[offset + 2:])
                    print(str(item))
                    
            elif tag == 0xAC:
                print("Encrypted signature:")
                print_hexdump(data, colored=True, header=True)
                signature = PUBLIC_KEY.encrypt(bytes(reversed(data)), None)[0]
                print("\n");
                
                print("Decrypted signature (DER):")
                print_hexdump(signature, colored=True, header=True, folded=True)
                print("\n");

                signature = signature.split(b'\x00', 1)[1]
                try:
                    assert signature[0] == 0x30
                    l = signature[1]
                    signature = signature[2:2+l]
                    assert signature[0] == 0x30

                    l = signature[1]
                    algo = signature[2:2+l]
                    hashsum = signature[2+l:]

                    assert hashsum[0] == 0x4
                    l = hashsum[1]
                    hashsum = hashsum[2:l+2]
                    print("Hash:", hashsum.hex())
                    print("\n");

                except:
                    pass
            
            elif tag == 0x5C:
                continue;
                
            elif tag == 0x5D:
                continue;
            
            else:
                raise ValueError("Parsing error. Unknown tag {:02x}".format(tag))
        except IndexError:
            break

if __name__ == '__main__':
    main()

#
# ** SCRIPT END **
#
