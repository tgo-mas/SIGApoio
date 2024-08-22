from rolepermissions.roles import AbstractUserRole

class Bolsista(AbstractUserRole):
    available_permissions = {
        'listar_emprestimos' : True,
        'listar_local' : True,
        'listar_recursos' : True,
        'listar_reservas' : True,
        'reservar_recurso': True,
    }
    
    
class Servidor(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuario' :True,
        'cadastrar_local' :True,
        'cadastrar_recurso': True,
        'cadastrar_tipo_recurso': True,
        'reservar_recurso': True,
        'listar_emprestimos': True,
        'listar_local': True,
        'listar_recursos': True,
        'cadastro_reserva_semanal': True,
        'cadastro_reserva_dia': True,
        'efetuar_chamados': True,
        'listar_reservas': True,
        
        
}
    
    

