from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('list', views.list, name='list'),
    path('fileupload', views.fileupload, name='fileupload'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('ajax/', views.ajax, name='ajax'),
    path('ajax/ajax', views.ajax, name='ajaxpost'),
    path('ajax/delete', views.ajax_delete, name='ajax_delete'),
    path('ajax/getajax', views.getajax, name='getajax'),
    path('register', views.register, name='register'),
    path('register/success/', views.register_success, name='register_success'),
    path('users/', views.users, name='users'),
    path('users/delete/<int:id>', views.user_delete, name='user_delete'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('change_password', views.changePassword, name='changePassword'),
    path('file/delete', views.changePassword, name='changePassword'),
    path('file/delete/<int:id>', views.deleteFiles, name='deleteFiles'),
    
    #paginas ventas
    path('ventas/',views.ventas, name='ventas'),
    path('ventas1/',views.ventas_uno, name='ventas1'),
    path('ventas2/',views.ventas_dos, name='ventas2'),
    path('ventas3/',views.ventas_tres, name='ventas3'),
    
    #paginas Puntos adicionales 
    path('puntosadicionales/',views.puntos_adicionales, name='puntosadicionales'),
    
    # Paginas registro de contratos
    path('registrodecontratos/',views.r_contratos, name='registrodecontratos'),
    path('registrodecontratosuno/',views.r_contratosuno, name='registrodecontratosuno'),
    path('registrodecontratosdos/',views.r_contratosdos, name='registrodecontratosdos'),
    path('registrodecontratostres/',views.r_contratostres, name='registrodecontratostres'),
    
    #Paginas soporte
    path('soporte/',views.soporte, name='soporte'),
    path('soporte1/',views.soporteuno, name='soporte1'),
    path('soporte2/',views.soportedos, name='soporte2'),
    path('soporte3/',views.soportetres, name='soporte3'),
    path('soporte4/',views.soportecuatro, name='soporte4'),
    path('clave/',views.clave, name='clave'),
    
    #Paginas PQR
    #path('', views. , name = ''),
    path('pqr/', views.pqr, name = 'pqr'),
    path('pqr1/', views.pqruno, name = 'pqr1'),
    path('pqr2/', views.pqrdos, name = 'pqr2'),
    
    #Paginas cambio de plan
    path('cplan/', views.cambioplan , name = 'cplan'),
    path('cplan1/', views.cambioplanuno , name = 'cplan1'),
    path('cplan2/', views.cambioplandos , name = 'cplan2'),
    path('cplan3/', views.cambioplantres , name = 'cplan3'),
    
    #Pagina cambio de titularidad
    path('titularidad/', views.titularidad , name = 'titularidad'),
    
    #Paginas desistimiento
    path('desistimiento/', views.desistimiento , name = 'desistimiento'),
    path('desistimiento1/', views.desistimientouno , name = 'desistimiento1'),
    path('desistimiento2/', views.desistimientodos , name = 'desistimiento2'),
    
    #Paginas Reconexiones
    path('reconexiones/', views.reconexiones , name = 'reconexiones'),
    
    #Paginas Traslados
    path('traslados/', views.traslados , name = 'traslados'),
    path('traslados1/', views.trasladosuno , name = 'traslados1'),
    path('traslados2/', views.trasladosdos , name = 'traslados2'),
    path('traslados3/', views.trasladostres , name = 'traslados3'),
    
    #Paginas suspenciones
    path('suspenciones/', views.suspenciones , name = 'suspenciones'),
    path('suspenciones1/', views.suspencionesuno , name = 'suspenciones1'),
    
    #Pagina pagos
    path('pagos/', views.pagos , name = 'pagos'),
    path('pagos1/', views.pagosuno, name = 'pagos1'),
    
    #Solicitud usuarios
    path('suser/', views.suser , name = 'suser'),
    
    
    #soporte
    
    
    
    
    
    
]
