from bitFont import BitFont
font = BitFont(
	height = 16,
	pixBytes = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x17\xf8\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00x\x00\x00\x00x\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x02@\x1e\xc0\x1f\xf8\x03x\x1e\xc0\x1f\xf8\x03x\x02@\x00\x00\x00\xe0\x08\xf0\x19\x10\x11\x18q\x18q\x10\x110\x1f \x0e\x00\x00\x00\x00\x10\x088\x0c(\x068\x03\x90\t\xc0\x1c`\x140\x1c\x10\x08\x00\x00\x00\x0ep\x1f\xf8\x11\x88\x11\x08\x13\x18\x1e\x10\x0c\x00\x1e\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00x\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x1f\xf0\x7f8\xe0\x08\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x808\xe0\xf0\x7f\xc0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xa0\x02\xe0\x03\xe0\x03\xe0\x03\xe0\x03\xa0\x02\x80\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\xe0\x0f\xe0\x0f\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x008\x008\x00\x18\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x0c\x00\x06\x00\x03\x80\x01\xc0\x00`\x000\x00\x10\x00\x00\x00\x00\x00\xf0\x0f\xf8\x1f\x08\x10\x08\x10\x08\x10\xf8\x1f\xf0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x10\x10\xf8\x1f\xf8\x1f\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x10\x18\x18\x1c\x08\x16\x08\x13\x88\x11\xf8\x10p\x10\x00\x00\x00\x00\x00\x00\x10\x08\x18\x18\x88\x10\x88\x10\x88\x10\xf8\x1fp\x0f\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\xe0\x02p\x12\xf8\x1f\xf8\x1f\x00\x12\x00\x00\x00\x00\x00\x00\xf8\x08\xf8\x18\x88\x10\x88\x10\x88\x10\x88\x1f\x08\x0f\x00\x00\x00\x00\x00\x00\xe0\x0f\xf0\x1f\x98\x11\x88\x10\x88\x10\x88\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x18\x00\x18\x18\x08\x1e\x88\x07\xe8\x01x\x00\x18\x00\x00\x00\x00\x00\x00\x00p\x0f\xf8\x1f\x88\x10\x88\x10\x88\x10\xf8\x1fp\x0f\x00\x00\x00\x00\x00\x00\xf0\x00\xf8\x11\x08\x11\x08\x11\x88\x19\xf8\x0f\xf0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x18\xc0\x18\xc0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \xc08\xc08\xc0\x18\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x03\xc0\x06`\x0c0\x18\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x80\x02\x80\x02\x80\x02\x80\x02\x80\x02\x80\x02\x80\x02\x00\x00\x00\x00\x00\x00\x10\x100\x18`\x0c\xc0\x06\x80\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x18\x00\x08\x16\x08\x17\x88\x01\xf8\x00p\x00\x00\x00\x00\x00\xe0\x0f\xf0\x1f\x983\xc8\'H$\xc8\'\xd8\'\xf0\'\xe0\x03\x00\x10\x00\x1c\x88\x1f\xe8\x13x\x02x\x02\xe0\x13\x80\x1f\x00\x1c\x00\x10\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x88\x10\x88\x10\x88\x10\xf8\x1fp\x0f\x00\x00\x00\x00\xe0\x07\xf0\x0f\x18\x18\x08\x10\x08\x10\x18\x10x\x18x\x08\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x08\x10\x08\x10\x18\x18\xf0\x0f\xe0\x07\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x88\x10\xc8\x11\xc8\x11\x18\x18\x18\x18\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x88\x10\xc8\x11\xc8\x01\x18\x00\x18\x00\x00\x00\x00\x00\xe0\x07\xf0\x0f\x18\x18\x08\x10\x08\x11\x18\x11x\x1fx\x0f\x00\x01\x08\x10\xf8\x1f\xf8\x1f\x88\x10\x80\x00\x80\x00\x88\x10\xf8\x1f\xf8\x1f\x08\x10\x00\x00\x00\x00\x08\x10\x08\x10\xf8\x1f\xf8\x1f\x08\x10\x08\x10\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1c\x00\x10\x08\x10\x08\x10\xf8\x1f\xf8\x0f\x08\x00\x08\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x88\x11\xe8\x03x\x06\x18\x1c\x08\x18\x00\x10\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x08\x10\x08\x10\x00\x10\x00\x18\x00\x18\x00\x00\x08\x10\xf8\x1f\xf8\x1f\xe0\x11\x80\x07\x80\x07\xe0\x11\xf8\x1f\xf8\x1f\x08\x10\x08\x10\xf8\x1f\xf8\x1f\xe0\x10\xc0\x11\x08\x07\x08\x0e\xf8\x1f\xf8\x1f\x08\x00\x00\x00\xe0\x07\xf0\x0f\x18\x18\x08\x10\x08\x10\x18\x18\xf0\x0f\xe0\x07\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x08\x11\x08\x11\x08\x01\xf8\x01\xf0\x00\x00\x00\x00\x00\xe0\x07\xf0O\x18X\x08p\x080\x18x\xf0O\xe0G\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x08\x11\x08\x03\x08\x07\xf8\x1d\xf0\x18\x00\x10\x00\x00p\x1c\xf8\x1c\x88\x18\x88\x10\x88\x11\x18\x118\x1f8\x0e\x00\x00\x18\x00\x08\x00\x08\x10\x08\x10\xf8\x1f\xf8\x1f\x08\x10\x08\x10\x18\x00\x18\x00\x08\x00\xf8\x0f\xf8\x0f\x08\x18\x00\x10\x00\x10\x08\x18\xf8\x0f\xf8\x0f\x08\x00\x08\x008\x00\xf8\x01\xc8\x07\x00\x1e\x00\x1e\xc8\x07\xf8\x018\x00\x08\x00x\x00\x88\x03\x88\x1f\x80\x1f\xe0\x03\xe0\x03\x80\x1f\x88\x1f\xf8\x03x\x00\x08\x10\x18\x188\x1ch\x16\xc0\x03\xc0\x03h\x168\x1c\x18\x18\x08\x10\x08\x00\x18\x00x\x10\xe8\x10\x80\x1f\x80\x1f\xe8\x10x\x10\x18\x00\x08\x00\x00\x00\x18\x18\x18\x1c\x08\x16\x88\x13\xc8\x11h\x108\x18\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xff\xf8\xff\x08\x80\x08\x80\x00\x00\x00\x00\x00\x00\x10\x000\x00`\x00\xc0\x00\x80\x01\x00\x03\x00\x06\x00\x0c\x00\x08\x00\x00\x00\x00\x00\x00\x08\x80\x08\x80\xf8\xff\xf8\xff\x00\x00\x00\x00\x00\x00\x00\x00@\x00`\x000\x00\x18\x00\x18\x000\x00`\x00@\x00\x00\x00\x00@\x00@\x00@\x00@\x00@\x00@\x00@\x00@\x00@\x00@\x00\x00\x00\x00\x00\x00\x08\x00\x18\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e@\x1f@\x11@\x11@\x11\xc0\x1f\x80\x1f\x00\x10\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\xc0\x18@\x10\xc0\x18\x80\x0f\x80\x0f\x00\x00\x00\x00\x80\x0f\x80\x0f\xc0\x18@\x10@\x10\xc0\x18\xc0\x08\xc0\x08\x00\x00\x00\x00\x80\x0f\x80\x0f\xc0\x18@\x10\xc8\x18\xf8\x1f\xf8\x1f\x00\x10\x00\x00\x00\x00\x80\x0f\x80\x0f\xc0\x1a@\x12@\x12\xc0\x1a\x80\x0b\x80\x0b\x00\x00\x00\x00\x00\x00\x80\x10\xf0\x1f\xf8\x1f\x88\x10\x88\x10\x18\x00\x10\x00\x00\x00\x00\x00\x80g\x80\xe7\xc0\x8c@\x88\xc0\x8c\xc0\xff\xc0\x7f@\x00\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\xc0\x10@\x10\xc0\x1f\x80\x1f\x00\x10\x00\x00\x00\x00\x00\x00@\x10@\x10\xc8\x1f\xc8\x1f\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00@\x00\xc0@\x80@\x80\xc8\xff\xc8\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x08\x10\xf8\x1f\xf8\x1f\x00\x13\xc0\x17\xc0\x1c@\x18@\x10\x00\x00\x00\x00\x00\x00\x08\x10\x08\x10\xf8\x1f\xf8\x1f\x00\x10\x00\x10\x00\x00\x00\x00@\x10\xc0\x1f\xc0\x1f\xc0\x10\xc0\x1f\xc0\x1f\xc0\x10\xc0\x1f\xc0\x1f\x00\x10\x00\x00@\x10\xc0\x1f\xc0\x1f\xc0\x10@\x10\xc0\x1f\x80\x1f\x00\x10\x00\x00\x00\x00\x80\x0f\x80\x0f\xc0\x18@\x10@\x10\xc0\x18\x80\x0f\x80\x0f\x00\x00\x00\x00@\x80\xc0\xff\xc0\xff\xc0\x98@\x90\xc0\x18\x80\x0f\x80\x0f\x00\x00\x00\x00\x80\x0f\x80\x0f\xc0\x18@\x90\xc0\x98\xc0\xff\xc0\xff@\x80\x00\x00\x00\x00@\x10@\x10\xc0\x1f\xc0\x1f\xc0\x10@\x10@\x00\xc0\x00\x80\x00\x00\x00\x80\t\xc0\x1b@\x12@\x12@\x12@\x12\xc0\x1e\x80\x0c\x00\x00\x00\x00@\x00@\x00\xf0\x0f\xf0\x1f@\x10@\x10@\x18\x00\x08\x00\x00\x00\x00@\x00\xc0\x0f\xc0\x1f\x00\x10@\x18\xc0\x1f\xc0\x1f\x00\x10\x00\x00@\x00\xc0\x00\xc0\x03@\x0f\x00\x1c\x00\x1c@\x0f\xc0\x03\xc0\x00@\x00@\x00\xc0\x07\xc0\x1f@\x1f\xc0\x07\xc0\x07@\x1f\xc0\x1f\xc0\x07@\x00\x00\x00@\x10\xc0\x18\xc0\x1d@\x17@\x17\xc0\x1d\xc0\x18@\x10\x00\x00@\x00\xc0\x80\xc0\x83@\xcf\x00|\x00<@\x0f\xc0\x03\xc0\x00@\x00\x00\x00\xc0\x10\xc0\x18@\x1c@\x16@\x13\xc0\x11\xc0\x18@\x18\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\xf0\x7f\xf8\xfd\x08\x80\x08\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xff\xf8\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x80\x08\x80\xf8\xfd\xf0\x7f\x00\x02\x00\x02\x00\x00\x00\x000\x008\x00\x08\x00\x18\x000\x00 \x008\x00\x18\x00\x00\x00"),
	endCols = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950]
)