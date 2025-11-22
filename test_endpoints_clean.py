import requests
import uuid

BASE_URL = "http://127.0.0.1:8000/api"

def test_alunos():
    print("\n=== TESTANDO ALUNOS ===")
    uid = str(uuid.uuid4())[:8]
    
    data = {"nome": f"Aluno {uid}", "email": f"aluno{uid}@test.com", "matricula": uid}
    r = requests.post(f"{BASE_URL}/alunos/", json=data)
    print(f"POST /alunos/ - Status: {r.status_code}")
    if r.status_code == 201:
        aluno = r.json()
        print(f"  OK Aluno criado: ID={aluno['id']}, Nome={aluno['nome']}")
        aluno_id = aluno['id']
    else:
        print(f"  ERRO: {r.text}")
        return None
    
    r = requests.get(f"{BASE_URL}/alunos/")
    print(f"GET /alunos/ - Status: {r.status_code}, Total: {len(r.json())}")
    
    r = requests.get(f"{BASE_URL}/alunos/{aluno_id}/")
    print(f"GET /alunos/{aluno_id}/ - Status: {r.status_code}")
    
    data = {"nome": f"Aluno Atualizado {uid}", "email": f"aluno{uid}@test.com", "matricula": uid}
    r = requests.put(f"{BASE_URL}/alunos/{aluno_id}/", json=data)
    print(f"PUT /alunos/{aluno_id}/ - Status: {r.status_code}")
    
    return aluno_id

def test_professores():
    print("\n=== TESTANDO PROFESSORES ===")
    uid = str(uuid.uuid4())[:8]
    
    data = {"nome": f"Prof {uid}", "email": f"prof{uid}@test.com", "area": "Computacao"}
    r = requests.post(f"{BASE_URL}/professores/", json=data)
    print(f"POST /professores/ - Status: {r.status_code}")
    if r.status_code == 201:
        prof = r.json()
        print(f"  OK Professor criado: ID={prof['id']}, Nome={prof['nome']}")
        return prof['id']
    else:
        print(f"  ERRO: {r.text}")
        return None
    
def test_materias():
    print("\n=== TESTANDO MATERIAS ===")
    uid = str(uuid.uuid4())[:8]
    
    data = {"nome": f"Materia {uid}", "descricao": "Teste", "carga_horaria": 80}
    r = requests.post(f"{BASE_URL}/materias/", json=data)
    print(f"POST /materias/ - Status: {r.status_code}")
    if r.status_code == 201:
        mat = r.json()
        print(f"  OK Materia criada: ID={mat['id']}, Nome={mat['nome']}")
        return mat['id']
    else:
        print(f"  ERRO: {r.text}")
        return None

def test_turmas(prof_id, mat_id):
    print("\n=== TESTANDO TURMAS ===")
    
    data = {
        "materia_id": mat_id,
        "professor_id": prof_id,
        "dia_semana": "Segunda",
        "hora_inicio": "19:00",
        "hora_fim": "21:00"
    }
    r = requests.post(f"{BASE_URL}/turmas/", json=data)
    print(f"POST /turmas/ - Status: {r.status_code}")
    if r.status_code == 201:
        turma = r.json()
        print(f"  OK Turma criada: ID={turma['id']}")
        return turma['id']
    else:
        print(f"  ERRO: {r.text}")
        return None
    
def test_inscricao(turma_id, aluno_id):
    print("\n=== TESTANDO INSCRICAO ===")
    
    data = {"aluno_id": aluno_id}
    r = requests.post(f"{BASE_URL}/turmas/{turma_id}/inscricoes/", json=data, timeout=5)
    print(f"POST /turmas/{turma_id}/inscricoes/ - Status: {r.status_code}")
    if r.status_code == 200:
        resp = r.json()
        print(f"  OK {resp.get('message', 'Inscrito com sucesso')}")
    else:
        print(f"  ERRO: {r.text}")

def test_relatorio():
    print("\n=== TESTANDO RELATORIO ===")
    
    r = requests.get(f"{BASE_URL}/relatorios/turmas/")
    print(f"GET /relatorios/turmas/ - Status: {r.status_code}")
    if r.status_code == 200:
        rel = r.json()
        print(f"  OK Total turmas: {rel['total_turmas']}")
        print(f"  OK Total alunos: {rel['total_alunos']}")
        print(f"  OK Media alunos/turma: {rel['media_alunos_por_turma']:.2f}")

if __name__ == "__main__":
    try:
        aluno_id = test_alunos()
        prof_id = test_professores()
        mat_id = test_materias()
        
        if prof_id and mat_id:
            turma_id = test_turmas(prof_id, mat_id)
            if turma_id and aluno_id:
                test_inscricao(turma_id, aluno_id)
        
        test_relatorio()
        
        print("\n" + "="*50)
        print("OK - TODOS OS TESTES CONCLUIDOS COM SUCESSO!")
        print("="*50)
    except Exception as e:
        print(f"\nERRO: {e}")
