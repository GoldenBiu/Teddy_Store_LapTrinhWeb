from django.contrib import admin
from django.urls import path, include
from Home import views as Phong
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),  # Trang admin của Django
    path('captcha/', include('captcha.urls')),
    path('', Phong.login, name='login'),  # Trang đăng nhập
    path('logout/', LogoutView.as_view(), name='logout'),
    path('phong/', Phong.phong_view, name='phong'),  
    path('phong/<int:phong_id>/', Phong.phong_detail, name='phong_detail'),
    
    path('dichvu/', Phong.dichvu_view, name='dichvu'),   
    path('them-dich-vu/', Phong.them_dich_vu, name='them_dich_vu'),  # Trang thêm dịch vụ
    path('suadichvu/<int:id>/', Phong.suadichvu, name='suadichvu'),
    path("xoa-dich-vu/<int:dich_vu_id>/", Phong.xoa_dich_vu, name="xoa_dich_vu"),
    path('suakh/<int:khach_hang_id>/', Phong.suakh, name='suakh'),
    path('xoa_khach_hang/<int:khach_hang_id>/', Phong.xoa_khach_hang, name='xoa_khach_hang'),
    path('ttctkh/<int:khach_hang_id>/', Phong.ttctkh, name='ttctkh'),
    path('phong/<int:phong_id>/', Phong.ttctphong, name='ttctphong'),
    path('khachhang/', Phong.kh, name='khachhang'),
    path('themkhachhang/', Phong.themkh, name='themkh'),
    path('themphong/', Phong.them_phong, name='themphong'),
    path('suaphong/<int:phong_id>/', Phong.suaphong, name='suaphong'),
    path('xoa_phong/<int:phong_id>/', Phong.xoa_phong, name='xoa_phong'),
    path('tim_kiem/', Phong.tim_kiem, name='tim_kiem'),
    path('tim-kiem-phi/', Phong.tim_kiem_phi, name='tim_kiem_phi'),  # Đường dẫn cho `tim_kiem_phi`
    path('them-hop-dong/<int:khach_hang_id>/', Phong.them_hop_dong, name='themhopdong'),
    path('quanlihopdong/', Phong.quan_li_hop_dong, name='quanlihopdong'),
    path('chisodien/', Phong.ChiSoDienNuoc_list, name='chisodien'),
    path('phi/', Phong.phat_sinh_view, name='phiphatsinh'),
    path('ttcthd/<int:HopDongID>/', Phong.ttcthd, name='ttcthd'),
    path('themphatsinh/', Phong.them_phi_phat_sinh, name='them_phi_phat_sinh'),
    path('delete_hop_dong/<int:hopdong_id>/', Phong.delete_hop_dong, name='delete_hop_dong'),
    path('edit_phatsinh/<int:phat_sinh_id>/', Phong.edit_phat_sinh, name='edit_phat_sinh'),
    path('delete_phatsinh/<int:phat_sinh_id>/', Phong.delete_phat_sinh, name='delete_phat_sinh'),  # Định nghĩa URL xóa
    path('chisodiennuoc/edit/<int:ChiSoID>/', Phong.edit_chisodiennuoc, name='edit_chisodiennuoc'),
    path('chisodien/edit/<int:ChiSoID>/', Phong.edit_chisodien, name='edit_chisodien'),
    path('them_phong/', Phong.them_phong_1, name='them_phong_1'),
    path('timp/', Phong.search_view, name='search_view'),
    path('tinhtien/', Phong.Hoadon, name='tinhtien'),
    path('edit_chisodien/<int:ChiSoID>/', Phong.edithoadon, name='edithoadon'),  # Chỉnh sửa ChiSoDienNuoc
    path('doanhthu/', Phong.doanhthu, name='doanhthu'),
    path('export_chisodiennuoc_excel/', Phong.export_chisodiennuoc_excel, name='export_chisodiennuoc_excel'),
    path('export_hopdong_excel/', Phong.export_hopdong_excel, name='export_hopdong_excel'),
    path('xoa_hoa_don/<int:chisoid>/', Phong.xoa_hoa_don, name='xoa_hoa_don'),
]

