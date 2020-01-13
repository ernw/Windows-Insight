 
def guid_structure_to_guid_representation(guid_structure):
    ''' 
        Takes as input the outputed format of windbg
        Example:
            0123 4567 89012345 678901234567 8901
            4648 bdb6 b675ec37 a23c4dc7fdf3 92bc
            -->
            B675EC37-BDB6-4648-BC92-F3FDC74D3CA2
    '''
    first_chunk = guid_structure[8:16]
    second_chunk = guid_structure[4:8]
    third_chunk = guid_structure[:4]
    forth_chunk = guid_structure[30:] + guid_structure[28:30] #LE
    norm_fifth_chunk = guid_structure[16:28][::-1] #LE
    norm_by_two_fifth_chunk = [norm_fifth_chunk[i:i+2] for i in range(0,len(norm_fifth_chunk),2)]
    fifth_chunk = "".join(map(lambda byte: byte[::-1],norm_by_two_fifth_chunk))
    return "-".join([first_chunk, second_chunk, third_chunk, forth_chunk, fifth_chunk])


def guid_representation_to_guid_structure(guid_representation):
    ''' 
        Takes as input the GUID format and outputs the windbg format
        Example:
            B675EC37-BDB6-4648-BC92-F3FDC74D3CA2
            -->
            4648bdb6`b675ec37 a23c4dc7`fdf392bc
    '''
    SEPARATOR = '`'
    SPACE = ' '
    guid_repr_lowered = guid_representation.lower()
    first,second,third,forth,fifth = guid_repr_lowered.split('-')
    guid_strc_fst_half = third + second + SEPARATOR + first
    guid_strc_snd_half = forth+fifth
    guid_strc_snd_half = [guid_strc_snd_half[i:i+2] for i in range(0,len(guid_strc_snd_half),2)][::-1]
    guid_strc_snd_half = "".join(guid_strc_snd_half[:4]) + SEPARATOR + "".join(guid_strc_snd_half[4:])
    return (guid_strc_fst_half + SPACE + guid_strc_snd_half).lower()
