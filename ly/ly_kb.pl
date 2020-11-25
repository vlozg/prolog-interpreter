%nha Tien Le
vua(leDaiHanh).
vo(duongVanNga,leDaiHanh).
cha(leDaiHanh,leThiPhatNgan).
cha(leDaiHanh,leLongDinh).
cha(leLongDinh,leTongThuan).

%ho Than, dan toc Tay.
vo(linhNamCongChua,thanThuaQuy).
cha(thanThuaQuy,thanThieuThai).
vo(binhDuongCongChua,thanThieuThai).
cha(thanThieuThai,thanCanhPhuc).
me(binhDuongCongChua,thanCanhPhuc).
vo(thienThanhCongChua,thanCanhPhuc).

%nha Ly

%vua Ly Thai To
vo(minhDucThaiHau,hienKhanhVuong).
cha(hienKhanhVuong,lyThaiTo).
me(minhDucThaiHau,lyThaiTo).
cha(hienKhanhVuong,vuUyVuong).
cha(hienKhanhVuong,ducThanhVuong).
me(minhDucThaiHau,vuUyVuong).
me(minhDucThaiHau,ducThanhVuong).

vua(lyThaiTo).
vo(leThiPhatNgan,lyCongUan).
cha(lyThaiTo,lyThaiTong).
cha(lyThaiTo,khaiQuocVuong).
cha(lyThaiTo,uyMinhHau).
cha(lyThaiTo,vuDucVuong).
cha(lyThaiTo,dongChinhVuong).
cha(lyThaiTo,anQuocCongChua).
cha(lyThaiTo,linhNamCongChua).
me(leThiPhatNgan,lyThaiTong).
me(leThiPhatNgan,khaiQuocVuong).
me(leThiPhatNgan,uyMinhHau).

% vua Ly Thai Tong
vua(lyThaiTong).
vo(linhCamHoangHau,lyThaiTong).
cha(lyThaiTong,lyThanhTong).
cha(lyThaiTong,phungCanVuong).
cha(lyThaiTong,binhDuongCongChua).
cha(lyThaiTong,truongNinhCongChua).
cha(lyThaiTong,kimThanhCongChua).
me(linhCamHoangHau,lyThanhTong).

%loan tam Vuong gianh ngai vang.
xungDot(ducThanhVuong,lyThaiTong).
cungPhe(ducThanhVuong,vuDucVuong).
cungPhe(ducThanhVuong,dongChinhVuong).

trungThan(lePhungHieu,lyThaiTong).
trungThan(quachThinhDat,lyThaiTong).

%ga cong chua
vo(binhDuongCongChua,thanThieuThai).
vo(truongNinhCongChua,haThieuLam).
vo(kimThanhCongChua,leTongThuan).
cha(leTongThuan,chauMucChanDang_hoLe).
me(kimThanhCongChua,chauMucChanDang_hoLe).

%vua Ly Thanh Tong
vua(lyThanhTong).
vo(thuongDuongHoangHau,lyThanhTong).
vo2(nguyenPhiYLan,lyThanhTong).
cha(lyThanhTong,lyNhanTong).
cha(lyThanhTong,minhNhanVuong).
cha(lyThanhTong,sungHienHau).
cha(lyThanhTong,thienThanhCongChua).
me(nguyenPhiYLan,lyNhanTong).
me(nguyenPhiYLan,minhNhanVuong).

trungThan(phungCanVuong,lyThanhTong).
trungThan(lyThuongKiet,lyThanhTong).
trungThan(lyDaoThanh,lyThanhTong).

cungPhe(thuongDuongHoangHau,lyDaoTong).
cungPhe(nguyenPhiYLan,lyThuongKiet).
xungDot(nguyenPhiYLan,thuongDuongHoangHau).

% gia pha Phung Can Vuong.
% con gai cua Phung Can Vuong duoc Thanh Tong nhan lam con, phong
% Ngoc Kieu cong chua, ga cho Chau muc Chan Dang ho Le.
% Theo mot vai suy doan, Du Tong Chinh Hoang co the la con trai cua
% Phung Can Vuong.

cha(phungCanVuong,ngocKieuCongChua).
congChua(ngocKieuCongChua,lyThanhTong).
cha(phungCanVuong,duTongChinhHoang).
cha(duTongChinhHoang,thuyThanhCongChua).

vo(ngocKieuCongChua,chauMucChanDang_hoLe).
cha(chauMucChanDang_hoLe,phuThienDaiVuong).
me(ngocKieuCongChua,phuThienDaiVuong).

vo(thuyThanhCongChua,phuThienDaiVuong).
cha(phuThienDaiVuong,camThanhPhuNhan).
cha(phuThienDaiVuong,phungThanhPhuNhan).
me(thuyThanhCongChua,camThanhPhuNhan).
me(thuyThanhCongChua,phungThanhPhuNhan).

% gia pha Sung Hien Hau.
vo(doPhuNhan,sungHienHau).
cha(sungHienHau,lyThanTong).
me(doPhuNhan,lyThanTong).
emTrai(doAnhVu,doPhuNhan).
chauGai(thucPhi_DoThuyChau,doAnhVu).
emTrai(doAnDi,thucPhi_DoThuyChau).

%vua Ly Nhan Tong
vua(lyNhanTong).
vo(lanAnhHoangHau,lyNhanTong).
vo(khamThienHoangHau,lyNhanTong).
vo(chanBaoHoangHau,lyNhanTong).
vo(thanhCucHoangHau,lyNhanTong).
vo(chieuThanhHoangHau,lyNhanTong).

trungThan(luuKhanhDam,lyNhanTong).
trungThan(leBaNgoc,lyNhanTong).
trungThan(mauDuDo,lyNhanTong).

%vua Ly Than Tong
vua(lyThanTong).
vo(leThienHoangHau,lyThanTong).
vo2(camThanhPhuNhan,lyThanTong).
vo2(phungThanhPhuNhan,lyThanTong).
cha(lyThanTong,minhDaoVuong).
cha(lyThanTong,lyAnhTong).
me(camThanhPhuNhan,lyAnhTong).

trungThan(duongAnhNhi,lyThanTong).
trungThan(lyCongBinh,lyThanTong).
trungThan(toHienThanh,lyThanTong).


%vua Ly Anh Tong
vua(lyAnhTong).
vo(chieuLinhHoangHau,lyAnhTong).
vo2(thucPhi_DoThuyChau,lyAnhTong).
xungDot(chieuLinhHoangHau,thucPhi_DoThuyChau).
cha(lyAnhTong,baoQuocVuong).
me(chieuLinhHoangHau,baoQuocVuong).
cha(lyAnhTong,lyCaoTong).
me(thucPhi_DoThuyChau,lyCaoTong).

%loan Than Loi
xungDot(thanLoi,lyAnhTong).
trungThan(hoangNghiaHien,lyAnhTong).
trungThan(lyCongTin,lyAnhTong).

%loan Do Anh Vu
thanTu(vuCatDai,lyAnhTong).
thanTu(doAnhVu,lyAnhTong).
xungDot(vuCatDai,doAnhVu).
xungDot(duongTuMinh,doAnhVu).
xungDot(triMinhVuong,doAnhVu).

%vua Ly Cao Tong
vua(lyCaoTong).
vo(anToanHoangHau,lyCaoTong).
cha(lyCaoTong,lyHueTong).
me(anToanHoangHau,lyHueTong).
emTrai(damDiMong,anToanHoangHau).


trungThan(doKinhTu,lyCaoTong).
thanTu(phamBinhDi,lyCaoTong).
thanTu(phamDu,lyCaoTong).
thanTu(quachBoc,lyCaoTong).

xungDot(doanThuong,lyCaoTong).
cungPhe(doanThuong,doanChu).
cungPhe(doanThuong,phamDu).

xungDot(phamBinhDi,phamDu).
cungPhe(quachBoc,phamBinhDi).

%vua Ly Hue Tong
vua(lyHueTong).
vo(thuanTrinhPhuNhan,lyHueTong).
cha(lyHueTong,lyChieuHoang).
cha(lyHueTong,thuanThienCongChua).
me(thuanTrinhPhuNhan,lyChieuHoang).
me(thuanTrinhPhuNhan,thuanThienCongChua).

thanTu(toTrungTu,lyHueTong).

%vua Ly Chieu Hoang
vua(lyChieuHoang).

%gia toc ho Tran
% Tran Thu Do là em ho cua 3 nguoi Tran Thua, Tran Tu
% Khanh, Thuan Trinh Phu Nhan.
cha(tranLy,thuanTrinhPhuNhan).
cha(tranLy,tranThua).
cha(tranLy,tranTuKhanh).
me(toPhong,thuanTrinhPhuNhan).
me(toPhong,tranThua).
me(toPhong,tranTuKhanh).
emHo(tranThuDo,thuanTrinhPhuNhan).

vo(thuanTuHoangHau,tranThua).
cha(tranThua,khamMinhDaiVuong).
cha(tranThua,tranThaiTong).
cha(tranThua,khamThienDaiVuong).
me(thuanTuHoangHau,khamMinhDaiVuong).
me(thuanTuHoangHau,tranThaiTong).
me(thuanTuHoangHau,khamThienDaiVuong).

vo(thuanThienCongChua,khamMinhDaiVuong).
vo(tranThiNguyet,khamMinhDaiVuong).

cha(khamMinhDaiVuong,hungNinhVuong).
cha(khamMinhDaiVuong,hungDaoVuong).
cha(khamMinhDaiVuong,nguyenThanhHoangHau).
me(tranThiNguyet,hungNinhVuong).
me(tranThiNguyet,hungDaoVuong).
me(tranThiNguyet,nguyenThanhHoangHau).

cha(khamMinhDaiVuong,vuThanhVuong).
cha(khamMinhDaiVuong,tinhQuocVuong).
me(thuanThienCongChua,vuThanhVuong).
me(thuanThienCongChua,tinhQuocVuong).

%vua Tran Thai Tong
vua(tranThaiTong).
vo(lyChieuHoang,tranThaiTong).
vo(thuanThienCongChua,tranThaiTong).
cha(tranThaiTong,tranThanhTong).
cha(tranThaiTong,chieuMinhVuong).
me(thuanThienCongChua,tranThanhTong).
me(thuanThienCongChua,chieuMinhVuong).

%vua Tran Thanh Tong.
vua(tranThanhTong).
vo(nguyenThanhHoangHau,tranThanhTong).


trungThan(X,Y):- trungThan(X,Z),vua(Z),cha(Z,Y),vua(Y).
phoMa(X,Z):- vo(Y,X),congChua(Y,Z).
congChua(X,Y):- cha(Y,X),vua(Y),nu(X).
nu(X):- vo(X,Y);vo2(X,Y).
phanNghich(X,Y):- (xungDot(X,Y);cungPhe(Z,X),xungDot(Z,Y)),vua(Y).
ngoaiThich(X):- (emTrai(X,Y);emHo(X,Y);cha(X,Y);anhChiEmRuot(X,Y);anhChiEm(X,Y)),(vo(Y,Z);me(Y,Z)),vua(Z).
ngoaiThich_chuyen_quyen(X,Z):- (emTrai(X,Y);chauGai(Y,X)),(me(Y,Z);vo(Y,Z);vo2(Y,Z)),vua(Z).
kiemCheQuyenLuc(X,Y):- trungThan(X,Z),vua(Z),ngoaiThich_chuyen_quyen(Y,Z).
gianThan(X,Y):- vua(Y),cungPhe(X,Z),xungDot(Z,Y),thanTu(X,Y).
xungDot(X,Z):- xungDot(Y,Z),cungPhe(Y,X).
cungPhe(X,Y):- cungPhe(Z,X),cungPhe(Z,Y).
keThu(X,Y):- xungDot(X,Z),trungThan(Y,Z),vua(Z).
hoangHau(X,Y):- vo(X,Y),vua(Y).
thaiHau(X):- me(X,Y),vua(Y).
anhChiEmRuot(X,Y):- me(Z,X),me(Z,Y),cha(W,X),cha(W,Y),(vo(Z,W);vo2(Z,W)).
anhChiEm(X,Y):- cha(W,X),cha(W,Y).
thanTu(X,Y):-(anhChiEm(X,Y);anhChiEmRuot(X,Y);phoMa(X,Y);trungThan(X,Y);ngoaiThich(X);ngoaiThich_chuyen_quyen(X,Y)),vua(Y).
con(X,Y):- cha(Y,X);me(Y,X).
chau(X,Y):- con(X,Z),con(Z,Y).
hauDue(X,Y):- con(X,Y);chau(X,Y);chau(X,Z),con(Z,Y);chau(X,W),chau(W,Y),chau(X,W),chau(W,Q),con(Q,Y);chau(X,W),chau(W,Q),chau(Q,Y).
ong(X,Y):- cha(X,Z),cha(Z,Y).
toTien(X,Y):- hauDue(Y,X).
