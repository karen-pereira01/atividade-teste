from src.service.service_user import ServiceUser

class TestServiceUser:

    #Cenários de testes para validar a função de adicionar usuários.
    def test_add_user_success(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuario adicionado com sucesso'
        service = ServiceUser()
        result = service.add_user(name=name_add, job=job_add)
        assert result_expect == result

    def test_add_user_exits(self):
        name_exits = 'Thiago'
        job_exits = 'Tester'
        result_expect = 'Usuario ja cadastrado'
        service = ServiceUser()
        result = service.add_user(name=name_exits, job=job_exits)
        assert result_expect == result

    def test_add_user_fail(self):
        name_fail = None
        job_fail = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()
        result = service.add_user(name=name_fail, job=job_fail)
        assert result_expect == result

    def test_add_user_name_and_job_wrong(self):
        name_wrong = 123
        job_wrong= 789
        result_expect = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()
        result = service.add_user(name=name_wrong, job=job_wrong)
        assert result_expect == result    

    def test_add_user_name_wrong(self):
        name_wrong = 123
        job_valid= 'TI'
        result_expect = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()
        result = service.add_user(name=name_wrong, job=job_valid)
        assert result_expect == result

    def test_add_user_job_wrong(self):
        name_valid = 'Marcela'
        job_wrong = 458
        result_expect = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()
        result = service.add_user(name=name_valid, job=job_wrong)
        assert result_expect == result

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()
        result = service.add_user(name=name_null, job=job_null)
        assert result_expect == result      

    #Cenários de testes para validar a função de atualizar usuários
    def test_user_update(self):
        name_update = 'Carlos'
        job_update = 'Carpinteiro'
        result_expect = 'Profissão atualizada com sucesso'
        service = ServiceUser()
        result = service.update_user(name=name_update, new_job=job_update)
        assert result_expect == result
    
    def test_user_update_not_found(self):
        name_update = 'Flora'
        job_update = 'Carpinteiro'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()
        result = service.update_user(name=name_update, new_job=job_update)
        assert result_expect == result

    #Cenários de testes para validar a função de deletar usuários
    def test_del_user(self):
        name_del = 'Ana'
        result_expect = 'Usuario removido'
        service = ServiceUser()
        result = service.del_user(name=name_del)
        assert result_expect == result
    
    def test_del_user_not_found(self):
        name_del = 'Carolina'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()
        result = service.del_user(name=name_del)
        assert result_expect == result
    
    #Cenários de testes para validar a função de pesquisar usuário
    def test_select_user(self):
        name_select = 'Ricardo'
        result_expect = 'Profissão: Cibersegurança'
        service = ServiceUser()
        result = service.select_user(name=name_select)
        assert result_expect == result

    def test_select_user_not_found(self):
        name_select = 'Valquiria'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()
        result = service.select_user(name=name_select)
        assert result_expect == result    

    
  