import json


def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
    }
    
    response = client.post("/jobs/create-job/", json=data)
    assert response.status_code == 200
    # assert response.json()["company"] == "doogle"
    # assert response.json()["description"] == "python"


def test_read_all_jobs(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/create-job/", json=data)
    client.post("/jobs/create-job/", json=data)

    response = client.get("/jobs/all/")
    print(f'{response.json()=}')
    assert response.status_code == 200
    assert response.json()
    # assert response.json()[0]
    # assert response.json()[1]

def test_update_a_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20"
        }
    client.post("/jobs/create-job/",json=data)
    data["title"] = "test new title"
    response = client.put("/jobs/update/1",json=data)
    # assert response.json()["msg"] == "Successfully updated data."

def test_delete_a_job(client):            #new
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20"
        }
    client.post("/jobs/create-job/",json=data)
    msg = client.delete("/jobs/delete/1")
    response = client.get("/jobs/get/1/")
    print(f'{response.text=}')
    assert response.status_code == status.HTTP_404_NOT_FOUND
