from bitFont import BitFont
font = BitFont(
	height = 38,
	pixBytes = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\x01|\x00\xf0\xff?\x1f\x00\xfc\xff\xcf\x07\x00\xff\xff\xf3\x01\xc0\xff\x01|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x01\x00\x00\x00\xff\x01\x00\x00\xc0\x7f\x00\x00\x00\xf0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x07\x00\x00\x00\xfc\x07\x00\x00\x00\xff\x01\x00\x00\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\x00\x00\xf0\xf0\x00\x00\x00<\xbc\x0f\x00\x00\x0f\xff\x03\x00\xc0\xff\xff\x00\x00\xfe\xff\x0f\x00\xf8\xff?\x00\x00\xfe\x1f\x0f\x00\x80\xff\xc3\xc3\x00`\xf0\xf0?\x00\x00<\xfe\x0f\x00\x00\xff\xff\x03\x00\xfe\xff\x0f\x00\xe0\xff\xff\x00\x00\xf8?<\x00\x00>\x0f\x0f\x00\x00\xc0\xc3\x03\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x01\x07\x00\x00\xff\xc0\x07\x00\xe0\x7f\xf0\x03\x00\xf8\x1f\xfc\x00\x00\x9f\x0f<\x00\xc0\xc3\x03\x1e\x00p\xf0\x80\x07\x00\xff\xff\xff\x0f\xc0\xff\xff\xff\x03\xc0\x81\x0f\x1e\x00\xf0\xc0\x83\x07\x00\xfc\xf0\xf9\x00\x00~\xf8?\x00\x80\x1f\xfe\x07\x00\xc0\x07\xff\x01\x00\xc0\x81\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\xf0\x0f\x00\x00\x00\xfe\x07\x00\x00\x80\xc3\x01\x00\x00p\xe0\x00\x00\x00\x1c8\x00\x00\x00\x07\x0e`\x00\x80\xc3\x01\x1e\x00\xe0\x7f\xc0\x03\x00\xf0\x0f|\x00\x00\xf0\xc0\x07\x00\x00\x00|\x00\x00\x00\xc0\x07\x00\x00\x00|\x00\x00\x00\xc0\x07\x00\x00\x00x\xe0\x01\x00\x80\x0f\xfe\x01\x00\xf8\xc0\xff\x00\x00\x0fp8\x00\xc0\x00\x0e\x1c\x00\x00\x80\x03\x07\x00\x00\xe0\xc0\x01\x00\x00p8\x00\x00\x00\xfc\x0f\x00\x00\x00\xfe\x01\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x07\x00\x00\x00\xfe\x07\x00\x80\xc1\xff\x01\x00\xfc\xf1\xff\x00\x80\xff?>\x00\xe0\xff\x07\x1f\x00\xfc\xff\x80\x07\x00\x8f?\xe0\x01\xc0\xc3?x\x00\xf0\xf0\x1f\x1e\x00\xfc\xff\xcf\x03\x00\xfe\xf7\xf7\x00\x80\xff\xf0\x1f\x00\xc0\x0f\xf8\x03\x00\x00\x00\xfe\x01\x00\x00\xf0\xff\x00\x00\x00\xfc>\x00\x00\x00\x1f\x0f\x00\x00\xc0\x80\x03\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x1f\x00\x00\x00\xf0\x1f\x00\x00\x00\xfc\x07\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x0f\x00\x00\xe0\xff?\x00\x00\xff\xff?\x00\xf0\xff\xff?\x00\xfe\x03\xf8?\xc0\x0f\x00\xc0\x1f\xf0\x00\x00\x80\x07\x0c\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x80\x01\x0f\x00\x00x\xc0\x0f\x00\xc0\x1f\xe0?\x80\xff\x03\xf0\xff\xff?\x00\xf0\xff\xff\x03\x00\xe0\xff\x1f\x00\x00\xc0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\xe0\x19\x00\x00\x00p\x0f\x00\x00\x00\xf8\x01\x00\x00\xe0?\x00\x00\x00\xf8\x0f\x00\x00\x00\xe0\x07\x00\x00\x00\xdc\x03\x00\x00\x80g\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x80\xff\x7f\x00\x00\xe0\xff\x1f\x00\x00\xf8\xff\x07\x00\x00\xfe\xff\x01\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x87\x01\x00\x00\xf01\x00\x00\x00|\x0e\x00\x00\x00\xff\x01\x00\x00\xc0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x0f\x00\x00\x00\xe0\x03\x00\x00\x00\xf8\x00\x00\x00\x00>\x00\x00\x00\x80\x0f\x00\x00\x00\xe0\x03\x00\x00\x00\xf8\x00\x00\x00\x00>\x00\x00\x00\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x07\x00\x00\x00\xf0\x01\x00\x00\x00|\x00\x00\x00\x00\x1f\x00\x00\x00\xc0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\xf0\x07\x00\x00\x80?\x00\x00\x00\xfe\x01\x00\x00\xf8\x07\x00\x00\xc0?\x00\x00\x00\xff\x00\x00\x00\xc0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\x0f\x00\x00\xfc\xff\x0f\x00\x80\xff\xff\x07\x00\xf0\xff\xff\x03\x00\xfe\x01\xfe\x01\x80\x0f\x00|\x00\xe0\x01\x00\x1e\x00x\x00\x80\x07\x00\x1e\x00\xe0\x01\x80\x0f\x00|\x00\xe0\x1f\xe0\x1f\x00\xf0\xff\xff\x03\x00\xf8\xff\x7f\x00\x00\xfc\xff\x0f\x00\x00\xfc\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\xc0\x01\x00\x00\x00p\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xf0\x01\x00\x00\x00\xfe\xff\x7f\x00\xc0\xff\xff\x1f\x00\xf0\xff\xff\x07\x00\xfc\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x03\xf0\x01\x00\xfe\x00~\x00\xc0?\xc0\x1f\x00\xf0\x0f\xf8\x07\x00\xfe\x00\xff\x01\x80\x0f\xe0\x7f\x00\xe0\x01\xf8\x1e\x00x\x00\x9f\x07\x00\x1e\xe0\xe3\x01\x80\x0f|x\x00\xe0\xc7\x1f\x1e\x00\xf0\xff\x83\x07\x00\xfc\x7f\xe0\x01\x00\xfe\x0fx\x00\x00\xff\x01\x1e\x00\x00\x1f\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\xe0\x01\x00\xe0\x07\xf8\x01\x00\xfc\x01\xfe\x00\x00\x7f\x80?\x00\xe0\x03\x00\x1f\x00x\x00\x80\x07\x00\x1e8\xe0\x01\x80\x07\x0ex\x00\xe0\x81\x03\x1e\x00x\xf0\x81\x07\x00~\xfe\xf8\x01\x00\xff\xff?\x00\xc0\xff\xfe\x0f\x00\xe0\x9f\xff\x01\x00\xe0\xc3?\x00\x00\x00\xe0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x0f\x00\x00\x00\xfc\x03\x00\x00\x80\xff\x00\x00\x00\xf8=\x00\x00\x80\x1f\x0f\x00\x00\xf0\xc3\x03\x00\x00?\xf0\x00\x00\xe0\x03<\x00\x00~\x00\x0f\x00\x80\xff\xff\x7f\x00\xe0\xff\xff\x1f\x00\xf8\xff\xff\x07\x00\xfe\xff\xff\x01\x00\x00\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x01\x00\x00\xff\xf0\x01\x00\xfe?\xfc\x00\x80\xff\x0f?\x00\xe0\xff\x03\x1f\x00xp\x80\x07\x00\x1e\x1e\xe0\x01\x80\x87\x07x\x00\xe0\xe1\x01\x1e\x00x\xf8\xc0\x07\x00\x1e\xfe\xfc\x00\x80\x07\xff?\x00\xe0\xc1\xff\x07\x00x\xe0\xff\x00\x00\x00\xe0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xff\x0f\x00\x00\xf8\xff\x0f\x00\x80\xff\xff\x07\x00\xf0\xff\xff\x03\x00|x\xf8\x00\x80\x0f\x0f|\x00\xe0\xe1\x01\x1e\x00xx\x80\x07\x00\x1e\x1e\xe0\x01\x80\x87\x0f|\x00\xe0\xe3\x87\x0f\x00\xf0\xf1\xff\x03\x00|\xfc\x7f\x00\x00\x1e\xfe\x0f\x00\x00\x07\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00x\x00\xe0\x01\xc0\x1f\x00x\x00\xfe\x07\x00\x1e\xe0\xff\x01\x80\x07\xfe\x7f\x00\xe0\xe1\xff\x01\x00x\xfc\x07\x00\x00\xde?\x00\x00\x80\xff\x03\x00\x00\xe0?\x00\x00\x00\xf8\x03\x00\x00\x00~\x00\x00\x00\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\xe0\xc3?\x00\x00\xfe\xf9\x1f\x00\xc0\xff\xff\x0f\x00\xf0\xff\xe3\x03\x00>~\xf0\x01\x80\x07\x0f|\x00\xe0\x80\x03\x1e\x008\xe0\x80\x07\x00\x0e8\xe0\x01\x80\x07\x0f|\x00\xe0\xe3\x07\x1f\x00\xf0\xff\xe3\x03\x00\xfc\xff\xff\x00\x00\xfe\xf9\x1f\x00\x00>\xfc\x01\x00\x00\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x81\x01\x00\xc0\xff\xe1\x01\x00\xf8\xffx\x00\x00\xff?>\x00\xc0\x87\x0f\x0f\x00\xf8\xc0\x87\x07\x00\x1e\xe0\xe1\x01\x80\x07xx\x00\xe0\x01\x1e\x1e\x00\xf8\xc0\xc3\x07\x00|x\xf8\x00\x00\xff\xff?\x00\x80\xff\xff\x07\x00\xc0\xff\x7f\x00\x00\xc0\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x01\x1f\x00\x00|\xc0\x07\x00\x00\x1f\xf0\x01\x00\xc0\x07|\x00\x00\xf0\x01\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x07|\x18\x00\xf0\x01\x1f\x03\x00|\xc0\xe7\x00\x00\x1f\xf0\x1f\x00\xc0\x07\xfc\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x00?\x00\x00\x00\xc0\x0f\x00\x00\x00\xf0\x03\x00\x00\x00\xfe\x01\x00\x00\x80\x7f\x00\x00\x00\xf0?\x00\x00\x00<\x0f\x00\x00\x00\xcf\x03\x00\x00\xe0\xf3\x01\x00\x00xx\x00\x00\x00\x1f>\x00\x00\xc0\x07\x0f\x00\x00\xf0\xc0\x03\x00\x00>\xf0\x01\x00\x80\x07x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x87\x07\x00\x00\xe0\xe1\x01\x00\x00xx\x00\x00\x00\x1e\x1e\x00\x00\x80\x87\x07\x00\x00\xe0\xe1\x01\x00\x00xx\x00\x00\x00\x1e\x1e\x00\x00\x80\x87\x07\x00\x00\xe0\xe1\x01\x00\x00xx\x00\x00\x00\x1e\x1e\x00\x00\x80\x87\x07\x00\x00\xe0\xe1\x01\x00\x00xx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\xe0\x01\x00\x80\x0f|\x00\x00\xc0\x03\x0f\x00\x00\xf0\xe1\x03\x00\x00xx\x00\x00\x00\x1e\x1e\x00\x00\x80\xcf\x07\x00\x00\xc0\xf3\x00\x00\x00\xf0<\x00\x00\x00\xfc\x0f\x00\x00\x00\xfe\x01\x00\x00\x80\x7f\x00\x00\x00\xc0\x0f\x00\x00\x00\xf0\x03\x00\x00\x00\xfc\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x01\x00\x00\x00\x7f\x00\x00\x00\xe0\x1f\x00\x00\x00\xf8\x07\x00\x00\x00\x7f\x00\x00\x00\xc0\x07\xc0|\x00\xf0\x00<\x1f\x00<\xc0\xcf\x07\x00\x0f\xf8\xf3\x01\xc0\x07\xff|\x00\xf0\xe3\x07\x00\x00\xf8\xff\x00\x00\x00\xfe?\x00\x00\x00\xff\x07\x00\x00\x80\xff\x00\x00\x00\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0?\x00\x00\x00\xfc?\x00\x00\xc0\xff?\x00\x00\xfc\x81\x1f\x00\x80\x0f\x80\x1f\x00\xf0\x01\x80\x07\x00\x1e\x00\xc0\x03\xc0\x03\xfc\xe0\x01p\xc0\x7fx\x00\x1e\xf8?<\x80\x03\x1f\x1f\x0f\xe0\xe0\x01\xc7\x03\x1c8\xc0\xe1\x00\x07\x07p8\xc0\xc1\x00\x1c\x0ep0\x80\x83\x03\x1c\x1cp\xe0\x00\x07\x8f\x1f8\xc0\x83\xff\x0f\x0f\xe0\xf0\xff\xc7\x018\xfc\xc1q\x00\x1e\x07p\x1c\x00\x0f\x00\x1c\x00\x80\x07\x80\x03\x00\xe0\x03\xf0\x00\x00\xf0\x83\x1f\x00\x00\xf0\xff\x03\x00\x00\xf8?\x00\x00\x00\xf0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\xe0\x01\x00\x00\x00\x7f\x00\x00\x00\xfc\x1f\x00\x00\xe0\xff\x07\x00\x00\xff\xff\x00\x00\xf8\xff\x07\x00\xc0\xff\xff\x00\x00\xfc\xff<\x00\x00\xff\x07\x0f\x00\xc0?\xc0\x03\x00\xf0\x0f\xf0\x00\x00\xfc\x1f<\x00\x00\xff?\x0f\x00\x00\xff\xff\x03\x00\x00\xfe\xff\x01\x00\x00\xfc\xff\x03\x00\x00\xf0\xff\x01\x00\x00\xe0\x7f\x00\x00\x00\xc0\x1f\x00\x00\x00\x80\x07\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xc0\x03\x1e\x00<\xf0\x80\x07\x00\x0f<\xe0\x01\xc0\x03\x0fx\x00\xf0\xc0\x03\x1e\x00<\xf0\x80\x07\x00\x0f<\xe0\x01\xc0\x87\x0fx\x00\xf0\xff\x07\x1f\x00\xf8\xff\xff\x07\x00\xfe\xff\xff\x00\x00\xff\xfc?\x00\x00\x1f\xfe\x07\x00\x00\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x03\x00\x00\xc0\xff\x07\x00\x00\xfc\xff\x07\x00\x80\xff\xff\x03\x00\xf0\xff\xff\x01\x00\xfe\x01\xff\x00\x80\x0f\x00?\x00\xf0\x01\x00\x1f\x00|\x00\xc0\x07\x00\x0f\x00\xe0\x01\xc0\x03\x00x\x00\xf0\x00\x00\x1e\x00<\x00\x80\x07\x00\x1f\x00\xf0\x01\xc0\x07\x00|\x00\xe0\x07\xc0\x0f\x00\xf8\x07\xfc\x03\x00\xfc\x01\x7f\x00\x00~\xc0\x0f\x00\x00\x1f\xf0\x01\x00\x00\x07\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\x03\x00x\x00\xf0\x00\x00\x1e\x00<\x00\x80\x07\x00\x0f\x00\xe0\x01\xc0\x03\x00x\x00\xf0\x00\x00\x1e\x00<\x00\x80\x07\x00\x1f\x00\xf0\x01\x80\x07\x00<\x00\xe0\x07\xc0\x0f\x00\xf8\x07\xfc\x03\x00\xfc\xff\x7f\x00\x00\xfe\xff\x0f\x00\x00\xff\xff\x01\x00\x00\xff\x1f\x00\x00\x00\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\x03\x0fx\x00\xf0\xc0\x03\x1e\x00<\xf0\x80\x07\x00\x0f<\xe0\x01\xc0\x03\x0fx\x00\xf0\xc0\x03\x1e\x00<\xf0\x80\x07\x00\x0f<\xe0\x01\xc0\x03\x0fx\x00\xf0\xc0\x03\x1e\x00<\xf0\x80\x07\x00\x0f\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00<\xf0\x00\x00\x00\x0f<\x00\x00\xc0\x03\x0f\x00\x00\xf0\xc0\x03\x00\x00<\xf0\x00\x00\x00\x0f<\x00\x00\xc0\x03\x0f\x00\x00\xf0\xc0\x03\x00\x00<\xf0\x00\x00\x00\x0f<\x00\x00\xc0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x7f\x00\x00\x00\xfc\xff\x00\x00\x80\xff\xff\x00\x00\xf8\xff\x7f\x00\x00\xff\xff\x1f\x00\xc0\x1f\xf0\x0f\x00\xf8\x01\xf0\x07\x00>\x00\xf0\x01\xc0\x07\x00|\x00\xf0\x01\x00\x1e\x00<\x00\x80\x07\x00\x0f\x00\xe0\x01\xc0\x03<x\x00\xf0\x00\x0f\x1e\x00|\xc0\xc3\x07\x00\x1f\xf0\xf0\x00\x80\x0f<>\x00\xe0\x0f\xff\x07\x00\xf0\xc3\xff\x00\x00\xf8\xf0\xff\x01\x00<\xfc\x7f\x00\x00\x0c\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\x00<\x00\x00\x00\x00\x0f\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x00\x0f\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x03\x00\x00\x00\xfe\x01\x00\x00\x80\xff\x00\x00\x00\xe0?\x00\x00\x00\xf8\x1f\x00\x00\x00\xc0\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\xc0\x07\x00\xff\xff\xff\x01\xc0\xff\xff?\x00\xf0\xff\xff\x0f\x00\xfc\xff\xff\x01\x00\xff\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\x00\xc0\x0f\x00\x00\x00\xf8\x01\x00\x00\x00\x7f\x00\x00\x00\xf0?\x00\x00\x00\xfe?\x00\x00\xc0\xff\x1f\x00\x00\xf8\xf3\x0f\x00\x00\x7f\xf0\x0f\x00\xf0\x07\xf8\x07\x00\xfc\x00\xfc\x07\x00\x1f\x00\xfc\x01\xc0\x03\x00~\x00p\x00\x00\x1e\x00\x0c\x00\x00\x07\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\x0f\x00\x00\x00\xfc\x7f\x00\x00\x00\xfc\xff\x03\x00\x00\xf0\xff\x0f\x00\x00\xc0\xff\x1f\x00\x00\x00\xff\x07\x00\x00\x00\xf8\x01\x00\x00\xf0\x7f\x00\x00\xc0\xff\x1f\x00\x00\xff\xff\x00\x00\xfc\xff\x03\x00\xc0\xff\x07\x00\x00\xf0\x0f\x00\x00\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\x80\x7f\x00\x00\x00\x80\x7f\x00\x00\x00\x80\x7f\x00\x00\x00\x80\x7f\x00\x00\x00\xc0?\x00\x00\x00\xc0?\x00\x00\x00\xc0?\x00\x00\x00\xc0?\x00\x00\x00\xc0?\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x03\x00\x00\xc0\xff\x07\x00\x00\xfc\xff\x07\x00\x80\xff\xff\x03\x00\xf0\xff\xff\x01\x00\xfe\x01\xff\x00\x80\x1f\x00?\x00\xf0\x03\x80\x1f\x00|\x00\xc0\x07\x00\x1f\x00\xf0\x01\xc0\x03\x00x\x00\xf0\x00\x00\x1e\x00<\x00\x80\x07\x00\x1f\x00\xf0\x01\xc0\x07\x00|\x00\xf0\x03\x80\x1f\x00\xf8\x01\xf0\x03\x00\xfe\x01\xff\x00\x00\xff\xff\x1f\x00\x80\xff\xff\x03\x00\xc0\xff\x7f\x00\x00\xc0\xff\x07\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\x00\x0f\x00\x00<\xc0\x03\x00\x00\x0f\xf0\x00\x00\xc0\x03<\x00\x00\xf0\x00\x0f\x00\x00<\xc0\x03\x00\x00\x1f\xf8\x00\x00\xc0\x0f\x1f\x00\x00\xe0\xff\x07\x00\x00\xf8\xff\x00\x00\x00\xfc?\x00\x00\x00\xfe\x07\x00\x00\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x1f\x00\x00\x00\xff\x1f\x00\x00\xf0\xff\x1f\x00\x00\xfe\xff\x0f\x00\xc0\xff\xff\x07\x00\xf8\x07\xfc\x03\x00~\x00\xfc\x00\xc0\x0f\x00~\x00\xf0\x01\x00\x1f\x00|\x00\xc0\x07\x00\x0f\x00\xe0\x01\xc0\x03\x00x\x00\xf0\x00`\x1e\x00|\x00\xbc\x07\x00\x1f\x80\xff\x01\xc0\x0f\xc0\x7f\x00\xe0\x07\xe0\x0f\x00\xf8\x07\xf0\x03\x00\xfc\xff\xff\x01\x00\xfe\xff\xff\x00\x00\xff\xff>\x00\x00\xff\x1f\x07\x00\x00\xff\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\x80\x07\x00\x00<\xe0\x01\x00\x00\x0fx\x00\x00\xc0\x03\x1e\x00\x00\xf0\x80\x07\x00\x00<\xe0\x01\x00\x00\x0fx\x00\x00\xc0\x03?\x00\x00\xf0\xe1\xff\x0f\x00\xfc\xff\xff\x07\x00\xfe\xff\xff\x01\x80\xff\xf3\x7f\x00\xc0\x7f\xf8\x1f\x00\xc0\x07\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\xf8\x80\x07\x00\x80\xff\xe0\x03\x00\xf0\x7f\xf8\x01\x00\xfe\x1f\xfe\x00\x80\xcf\x07>\x00\xf0\xe1\x03\x1f\x00<\xf8\x80\x07\x00\x0f<\xe0\x01\xc0\x03\x0fx\x00\xf0\xc0\x07\x1e\x00|\xf0\x81\x07\x00\x1fx\xf0\x01\x80\x1f><\x00\xe0\x8f\xff\x0f\x00\xf0\xc3\xff\x03\x00\xf8\xf0\x7f\x00\x008\xf8\x0f\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x00\x0f\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x00\x0f\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xff?\x00\x00\xff\xff?\x00\xc0\xff\xff\x1f\x00\xf0\xff\xff\x0f\x00\xfc\xff\xff\x03\x00\x00\x00\xf8\x01\x00\x00\x00|\x00\x00\x00\x00\x1f\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1f\x00\x00\x00\xc0\x07\x00\x00\x00\xf8\x01\xc0\xff\xff?\x00\xf0\xff\xff\x0f\x00\xfc\xff\xff\x01\x00\xff\xff?\x00\xc0\xff\xff\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00|\x00\x00\x00\x00\xff\x00\x00\x00\xc0\xff\x01\x00\x00\xf0\xff\x03\x00\x00\xf0\xff\x0f\x00\x00\xc0\xff\x1f\x00\x00\x80\xff?\x00\x00\x00\xfc\x1f\x00\x00\x00\xf8\x07\x00\x00\x00\xfe\x01\x00\x00\xf0\x7f\x00\x00\xe0\xff\x0f\x00\x00\xff\x7f\x00\x00\xfc\xff\x03\x00\xc0\xff\x0f\x00\x00\xf0\x7f\x00\x00\x00\xfc\x03\x00\x00\x00\x1f\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\xc0?\x00\x00\x00\xf0\xff\x00\x00\x00\xfc\xff\x03\x00\x00\xff\xff\x0f\x00\x00\xf8\xff\x1f\x00\x00\xc0\xff\x1f\x00\x00\x00\xfc\x07\x00\x00\x00\xff\x01\x00\x00\xff\x7f\x00\x00\xfe\xff\x07\x00\xfc\xff\x1f\x00\x00\xff?\x00\x00\xc0\x7f\x00\x00\x00\xf0\x1f\x00\x00\x00\xfc\xff\x00\x00\x00\xff\xff\x07\x00\x00\xf8\xff\x1f\x00\x00\xc0\xff\x1f\x00\x00\x00\xfc\x07\x00\x00\x00\xff\x01\x00\x00\xfe\x7f\x00\x00\xfe\xff\x07\x00\xfc\xff?\x00\x00\xff\xff\x00\x00\xc0\xff\x07\x00\x00\xf0\x1f\x00\x00\x00|\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x06\x00\x07\x00\xc0\x01\xc0\x03\x00|\x00\xf0\x03\xc0\x1f\x00\xfc\x03\xf8\x07\x00\xff\x83\xff\x01\x80\xff\xfb\x1f\x00\x80\xff\xff\x01\x00\x80\xff\x1f\x00\x00\x00\xff\x01\x00\x00\xe0\xff\x00\x00\x00\xfe\xff\x00\x00\xe0\xff\xff\x00\x00\xfe\xc7\xff\x00\xc0\x7f\xc0\x7f\x00\xf0\x07\xe0\x1f\x00|\x00\xe0\x07\x00\x0f\x00\xe0\x01\xc0\x00\x00`\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00p\x00\x00\x00\x00\xfc\x00\x00\x00\x00\xff\x00\x00\x00\xc0\xff\x00\x00\x00\xf0\xff\x00\x00\x00\xf0\xff\x01\x00\x00\xf0\xff\xff\x01\x00\xe0\xff\x7f\x00\x00\xe0\xff\x1f\x00\x00\xf8\xff\x07\x00\x80\xff\xff\x01\x00\xfc\x1f\x00\x00\xc0\xff\x01\x00\x00\xfc\x1f\x00\x00\x00\xff\x01\x00\x00\xc0\x1f\x00\x00\x00\xf0\x01\x00\x00\x00\x1c\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xc0\x07\x00\x0f\x00\xfc\x01\xc0\x03\x80\x7f\x00\xf0\x00\xf0\x1f\x00<\x00\xff\x07\x00\x0f\xe0\xff\x01\xc0\x03\xfe{\x00\xf0\xc0?\x1e\x00<\xf8\x87\x07\x00\x8f\x7f\xe0\x01\xc0\xf3\x0fx\x00\xf0\xfe\x01\x1e\x00\xfc\x1f\x80\x07\x00\xff\x03\xe0\x01\xc0?\x00x\x00\xf0\x07\x00\x1e\x00\xfc\x00\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x7f\xc0\xff\xff\xff\x1f\xf0\xff\xff\xff\x07\xfc\xff\xff\xff\x01\x07\x00\x00p\xc0\x01\x00\x00\x1cp\x00\x00\x00\x07\x1c\x00\x00\xc0\x01\x00\x00\x00\x00\xc0\x01\x00\x00\x00\xf0\x07\x00\x00\x00\xf0\x0f\x00\x00\x00\xe0\x1f\x00\x00\x00\xc0\x7f\x00\x00\x00\x80\xff\x00\x00\x00\x00\xfe\x01\x00\x00\x00\xfc\x01\x00\x00\x00x\x00p\x00\x00\x00\x07\x1c\x00\x00\xc0\x01\x07\x00\x00p\xc0\x01\x00\x00\x1c\xf0\xff\xff\xff\x07\xfc\xff\xff\xff\x01\xff\xff\xff\x7f\xc0\xff\xff\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\xf8\x00\x00\x00\xc0?\x00\x00\x00\xfc\x0f\x00\x00\xe0\x7f\x00\x00\x00\xfc\x03\x00\x00\x00?\x00\x00\x00\xc0\x0f\x00\x00\x00\xf0\x0f\x00\x00\x00\xf8\x1f\x00\x00\x00\xf0?\x00\x00\x00\xf0\x0f\x00\x00\x00\xe0\x03\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x18\x00\x00\x00\x00\x06\x00\x00\x00\x80\x01\x00\x00\x00`\x00\x00\x00\x00\x18\x00\x00\x00\x00\x06\x00\x00\x00\x80\x01\x00\x00\x00`\x00\x00\x00\x00\x18\x00\x00\x00\x00\x06\x00\x00\x00\x80\x01\x00\x00\x00`\x00\x00\x00\x00\x18\x00\x00\x00\x00\x06\x00\x00\x00\x80\x01\x00\x00\x00`\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\x01\x00\x00\x00x\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe1\x07\x00\x00x\xfc\x03\x00\x00\x9f\xff\x01\x00\xc0\xe7\x7f\x00\x00\xf8}\x1f\x00\x00\x1e\x87\x07\x00\x80\xc3\xe1\x01\x00\xe0px\x00\x008\x0e\x0e\x00\x00\x8e\xc3\x03\x00\x80\xe7x\x00\x00\xe0\xff\x7f\x00\x00\xf0\xff\x1f\x00\x00\xfc\xff\x07\x00\x00\xfc\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\x00\x80\x07\x1c\x00\x00\xf0\x00\x0e\x00\x00\x1e\x80\x03\x00\x80\x07\xe0\x01\x00\xe0\x01x\x00\x00x\x00\x1e\x00\x00>\xc0\x07\x00\x80?\xfc\x01\x00\xc0\xff?\x00\x00\xf0\xff\x07\x00\x00\xf0\xff\x00\x00\x00\xf0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x0f\x00\x00\x00\xfe\x0f\x00\x00\xe0\xff\x07\x00\x00\xfc\xff\x03\x00\x00\x1f\xf8\x00\x00\xe0\x03|\x00\x00x\x00\x1e\x00\x00\x1e\x80\x07\x00\x80\x07\xe0\x01\x00\xe0\x01x\x00\x00\xf8\x01\x1f\x00\x00\xfc\xf0\x03\x00\x00?\xfc\x00\x00\x80\x0f\x0f\x00\x00\x80\xc3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\xf0\xff\x00\x00\x00\xfe\x7f\x00\x00\xc0\xff?\x00\x00\xf8\x81\x1f\x00\x00>\xc0\x07\x00\x80\x07\xe0\x01\x00\xe0\x01x\x00\x00x\x00\x1e\x00\x00\x1e\x80\x03\x00\x00\x0f\xf0\x00\x00\x80\x07\x0e\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\xf0\xff\x00\x00\x00\xfe\x7f\x00\x00\xc0\xff?\x00\x00\xf0\x9d\x0f\x00\x00>\xc7\x07\x00\x80\xc7\xe1\x01\x00\xe0qx\x00\x00x\x1c\x1e\x00\x00\x1e\x87\x07\x00\x80\xcf\xf1\x00\x00\xc0\x7f>\x00\x00\xf0\x9f\x07\x00\x00\xf8\xe7\x01\x00\x00\xfc\x19\x00\x00\x00|\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x80\x03\x00\x00\x00\xe0\x00\x00\x00\xc0\xff\xff\x1f\x00\xf8\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf08\x00\x00\x00\x1c\x0e\x00\x00\x00\x87\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0?0\x00\x00\xfc?<\x00\x80\xff\x1f\x1f\x00\xf0\xff\xcf\x07\x00\xfe\xf0\xf7\x03\x80\x0f\xf0\xf1\x00\xe0\x01x<\x00x\x00\x1e\x0e\x00\x1e\x80\x87\x03\x80\x07\xe0\xf1\x00\xc0\x03<<\x00\xe0\xc3\xc7\x0f\x00\xfe\xff\xff\x01\x80\xff\xff\x7f\x00\xe0\xff\xff\x0f\x00\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\x00>\x00\x00\x00\xc0\x03\x00\x00\x00p\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00\xf8\x00\x00\x00\x00\xfc\xff\x07\x00\x00\xff\xff\x01\x00\x80\xff\x7f\x00\x00\x80\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcf\xff\xff\x01\xc0\xf3\xff\x7f\x00\xf0\xfc\xff\x1f\x00<\xff\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x03\x00\x00\x00\xf0\xc0\xf3\xff\xff?\xf0\xfc\xff\xff\x0f<\xff\xff\xff\x03\xcf\xff\xff?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\xc0\xff\xff\x7f\x00\x00\x00~\x00\x00\x00\xc0\x0f\x00\x00\x00\xf8\x03\x00\x00\x00\xff\x03\x00\x00\xe0\xff\x01\x00\x00|\xff\x01\x00\x80\x0f\xff\x01\x00\xe0\x01\x7f\x00\x008\x00\x1f\x00\x00\x06\x00\x07\x00\x80\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\x7f\x00\xf0\xff\xff\x1f\x00\xfc\xff\xff\x07\x00\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xff\x1f\x00\x00\xfe\xff\x07\x00\x80\xff\xff\x01\x00\xe0\xff\x7f\x00\x00\xe0\x01\x00\x00\x00<\x00\x00\x00\x00\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00>\x00\x00\x00\x80\xff\xff\x01\x00\xc0\xff\x7f\x00\x00\xf0\xff\x1f\x00\x00\xf8\xff\x07\x00\x00\x1f\x00\x00\x00\xc0\x03\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x03\x00\x00\x00\xf8\xff\x1f\x00\x00\xfc\xff\x07\x00\x00\xff\xff\x01\x00\x00\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xff\xff\x01\x00\xe0\xff\x7f\x00\x00\xf8\xff\x1f\x00\x00\xfe\xff\x07\x00\x00\x1e\x00\x00\x00\xc0\x03\x00\x00\x00p\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x07\x00\x00\x00\xe0\x01\x00\x00\x00\xf8\x00\x00\x00\x00\xfe\xff\x07\x00\x00\xff\xff\x01\x00\xc0\xff\x7f\x00\x00\xc0\xff\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0?\x00\x00\x00\xfc?\x00\x00\x80\xff\x1f\x00\x00\xf0\xff\x0f\x00\x00\xfc\xf0\x03\x00\x80\x0f\xf0\x01\x00\xe0\x01x\x00\x00x\x00\x1e\x00\x00\x1e\x80\x07\x00\x80\x07\xe0\x01\x00\xe0\x01x\x00\x00\xf8\x00\x1f\x00\x00\xfc\xf0\x03\x00\x00\xff\xff\x00\x00\x80\xff\x1f\x00\x00\xc0\xff\x03\x00\x00\xc0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xff\xff\xff\x00\xe0\xff\xff?\x00\xf8\xff\xff\x0f\x00\xfe\xff\xff\x03\x00>|\x00\x00\xc0\x03<\x00\x00p\x00\x0e\x00\x00\x1e\x80\x07\x00\x80\x07\xe0\x01\x00\xe0\x01x\x00\x00\xf8\x00\x1f\x00\x00\xfe\xf0\x07\x00\x00\xff\xff\x00\x00\x80\xff\x1f\x00\x00\xc0\xff\x03\x00\x00\xc0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0?\x00\x00\x00\xfc?\x00\x00\x80\xff?\x00\x00\xf0\xff\x0f\x00\x00|\xe0\x07\x00\x80\x0f\xf0\x01\x00\xe0\x01x\x00\x00x\x00\x1e\x00\x00\x1e\x80\x07\x00\x80\x07\xe0\x01\x00\xc0\x03<\x00\x00\xe0\x81\x07\x00\x00\xfe\xff\xff\x03\x80\xff\xff\xff\x00\xe0\xff\xff?\x00\xf8\xff\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xff\xff\x01\x00\xe0\xff\x7f\x00\x00\xf8\xff\x1f\x00\x00\xfe\xff\x07\x00\x00|\x00\x00\x00\x80\x07\x00\x00\x00\xf0\x00\x00\x00\x00<\x00\x00\x00\x80\x0f\x00\x00\x00\xe0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x1f\x1e\x00\x00\xe0\x8f\x0f\x00\x00\xfc\xe3\x03\x00\x00\xff\xf9\x01\x00\xe0yx\x00\x008<\x1c\x00\x00\x0e\x0f\x07\x00\x80\xc3\xc3\x01\x00\xe0\xf0p\x00\x00xx\x1c\x00\x00~\x9e\x07\x00\x00\x9f\xff\x00\x00\xc0\xc7?\x00\x00\xe0\xf1\x07\x00\x00`\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x80\x03\x00\x00\x00\xfe\xff\x1f\x00\x80\xff\xff\x0f\x00\xe0\xff\xff\x07\x00\xf8\xff\xff\x01\x00\xe0\x00x\x00\x008\x00\x1e\x00\x00\x0e\x80\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xff\x00\x00\x80\xff\xff\x00\x00\xe0\xff?\x00\x00\xf8\xff\x1f\x00\x00\x00\xe0\x07\x00\x00\x00\xe0\x01\x00\x00\x00x\x00\x00\x00\x00\x1e\x00\x00\x00\x80\x03\x00\x00\x00\xf0\x00\x00\x00\x00\x1e\x00\x00\xf8\xff\x1f\x00\x00\xfe\xff\x07\x00\x80\xff\xff\x01\x00\xe0\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00x\x00\x00\x00\x00\xfe\x00\x00\x00\x80\xff\x01\x00\x00\xe0\xff\x03\x00\x00\xe0\xff\x07\x00\x00\x80\xff\x07\x00\x00\x00\xfe\x01\x00\x00\x00|\x00\x00\x00\xe0\x1f\x00\x00\x80\xff\x07\x00\x00\xfe\x7f\x00\x00\xe0\xff\x03\x00\x00\xf8\x1f\x00\x00\x00\xfe\x00\x00\x00\x80\x07\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x01\x00\x00\x00\xe0\x03\x00\x00\x00\xf8\x0f\x00\x00\x00\xfe?\x00\x00\x80\xff\x7f\x00\x00\x00\xff\x7f\x00\x00\x00\xf0\x1f\x00\x00\x00\xe0\x07\x00\x00\x80\xff\x01\x00\x00\xfe\x1f\x00\x00\xf8\xff\x00\x00\x00\xfe\x03\x00\x00\x80?\x00\x00\x00\xe0?\x00\x00\x00\xf8\xff\x00\x00\x00\xe0\xff\x01\x00\x00\x80\xff\x01\x00\x00\x00~\x00\x00\x00\xf0\x1f\x00\x00\xf0\xff\x07\x00\x80\xff\x7f\x00\x00\xe0\xff\x03\x00\x00\xf8\x0f\x00\x00\x00>\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x06\x00\x80\x03\xc0\x01\x00\xe0\x03|\x00\x00\xf8\x81\x1f\x00\x00\xfe\xf8\x07\x00\x00\x7f\xff\x00\x00\x00\xff\x0f\x00\x00\x00\xff\x00\x00\x00\xc0?\x00\x00\x00\xfc?\x00\x00\xc0\xdf?\x00\x00\xf8\xc3\x1f\x00\x00~\xe0\x07\x00\x80\x07\xe0\x01\x00\xe0\x00p\x00\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00~\x00\x00\x00\x80\xff\x00\xf0\x00\xe0\xff\x01<\x00\xf8\xff\x83\x0f\x00\xe0\xff\xff\x03\x00\xc0\xff\x7f\x00\x00\x00\xff\x1f\x00\x00\xc0\xff\x01\x00\x00\xff\x1f\x00\x00\xfc\xff\x00\x00\xe0\xff\x07\x00\x00\xf8?\x00\x00\x00\xfe\x01\x00\x00\x80\x0f\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x01|\x00\x00x\x80\x1f\x00\x00\x1e\xf0\x07\x00\x80\x07\xff\x01\x00\xe0\xe1\x7f\x00\x00x\xfc\x1e\x00\x00\x9e\x9f\x07\x00\x80\xf7\xe3\x01\x00\xe0\x7fx\x00\x00\xf8\x0f\x1e\x00\x00\xfe\x81\x07\x00\x80?\xe0\x01\x00\xe0\x03x\x00\x00x\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\xc0\x07\x00\x00\xff\xff\xff\x0f\xe0\xff\xef\xff\x07\xfc\xff\xfb\xff\x03\xff\x7f\xfc\xff\xc0\x03\x00\x008p\x00\x00\x00\x0e\x1c\x00\x00\x80\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\xff\x1f\xf0\xff\xff\xff\x07\xfc\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x01\x00\x008p\x00\x00\x00\x0e<\x00\x00\x80\x03\xff\x7f\xfc\xff\xc0\xff\xbf\xff?\xe0\xff\xef\xff\x07\xf0\xff\xff\xff\x00\x00\xc0\x07\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x00\x1e\x00\x00\x00\xc0\x03\x00\x00\x00p\x00\x00\x00\x00\x1c\x00\x00\x00\x00\x0e\x00\x00\x00\x80\x03\x00\x00\x00\xc0\x01\x00\x00\x00p\x00\x00\x00\x008\x00\x00\x00\x00\x0e\x00\x00\x00\xc0\x03\x00\x00\x00x\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
	endCols = [9, 20, 36, 55, 73, 102, 126, 134, 145, 156, 169, 188, 197, 208, 217, 226, 244, 262, 280, 298, 316, 334, 352, 370, 388, 406, 417, 428, 447, 466, 485, 505, 538, 561, 585, 609, 633, 655, 675, 700, 723, 732, 750, 774, 794, 821, 845, 870, 892, 918, 942, 964, 984, 1008, 1030, 1061, 1083, 1105, 1125, 1136, 1145, 1156, 1175, 1193, 1204, 1222, 1242, 1260, 1280, 1298, 1309, 1329, 1349, 1358, 1367, 1386, 1395, 1425, 1445, 1465, 1485, 1505, 1518, 1537, 1548, 1568, 1587, 1613, 1632, 1651, 1668, 1681, 1690, 1703, 1722]
)