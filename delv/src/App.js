import './App.css';
import { useQuery, gql, useMutation } from "@apollo/client";
import { Button, Form, Input } from 'antd';
import React, { useState } from 'react';
import { Typography } from 'antd';
import { Divider } from 'antd';
import {  message , Modal, List, Skeleton } from 'antd';
import { DeleteFilled,EditFilled } from '@ant-design/icons';

const { Title } = Typography;
const CITIES_QUERY = gql`
{
	city  {
      id
      name
  }
}
`;


const CREATE_City = gql`
mutation createCity($name: String!) {
  createCity(name: $name) {
    city{
      id
      name
      }
  }
}
`;
const UPDATE_City = gql`
mutation updateCity($id: ID! , $name: String!) {
  updateCity(cityData:{id: $id, name: $name}) {
    city{
      id
      name
      }
  }
}
`;
const DELETE_City = gql`
mutation deleteCity($id: ID!) {
  deleteCity(id: $id) {
    city{
      id
      name
      }
  }
}
`;
const App = () => {
  const [form] = Form.useForm();
  const [formLayout, setFormLayout] = useState('horizontal');
  const onFormLayoutChange = ({ layout }) => {
    setFormLayout(layout);
  };
  const formItemLayout =
    formLayout === 'horizontal'
      ? {
        labelCol: {
          span: 4,
        },
        wrapperCol: {
          span: 14,
        },
      }
      : null;
  const buttonItemLayout =
    formLayout === 'horizontal'
      ? {
        wrapperCol: {
          span: 14,
          offset: 4,
        },
      }
      : null;
  const [formState, setFormState] = useState({
    name: '',
  });
  const [title, setTitle] = useState('');
  const [titleModify, setTitleModify] = useState('');
  const [selectedItem, setSelectedItem] = useState({});
  const [modal1Open, setModal1Open] = useState(false);
 

  const [createCity] = useMutation(CREATE_City, {
    variables: {
      name: formState.name,
    }
    ,
    onCompleted: () => {
      message.success('Ville créée avec succès');
      refetch();
    },
    onError: (error) => {
      message.error('Erreur lors de la création de la ville');

    }
  }); 
  
  const [updateCity] = useMutation(UPDATE_City, {
    variables: {
      name: formState.name,
      id: selectedItem.id,
    }
    ,
    onCompleted: () => {
      message.success('Ville mis a jour avec succès');
      setModal1Open(false);
      refetch();
    },
    onError: (error) => {
      message.error('Erreur lors de la mise a jour de la ville');

    }
  });

  const [deleteCity] = useMutation(DELETE_City, {
    variables: {
      id: selectedItem.id,
    }
    ,
    onCompleted: () => {
      message.success('Ville supprimé avec succès');
      refetch();
    },
    onError: (error) => {
      message.error('Erreur lors de la suppression de la ville');

    }
  });

  const { loading, error, data, refetch } = useQuery(CITIES_QUERY);
  if (loading) return "Loading...";
  if (error) return <pre>{error.message}</pre>
  console.log("data", data);



  const onNameChange = (value) => {
    setTitle(value.target.value);

  }
 const onEditNameChange = (value) => {
  setTitleModify(value.target.value);

  }

  const onFinish = (values) => {
    createCity({ variables: { name: title } });
  }; 
  
  const onEdit = (item) => {
    console.log("item",item);
    setTitleModify(item.name);
    setSelectedItem(item); 
    setModal1Open(true);
  };
  return (
    <div>    <Divider><Title>Ajouter ville</Title></Divider>


      <Form
        {...formItemLayout}
        layout={formLayout}
        form={form}
        initialValues={{
          layout: formLayout,
        }}
        onFinish={onFinish}
      //  onValuesChange={onFormLayoutChange}
      >
        <Form.Item label="Nom">
          <Input placeholder="nom de ville" onChange={onNameChange} />
        </Form.Item>
        <Form.Item {...buttonItemLayout}>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>      </Form.Item>
      </Form>
      <Divider><Title>Liste des villes</Title></Divider>
      
      <Modal
        title={"Modification ville #"+selectedItem?.id+" - "+selectedItem?.name+""}
        style={{
          top: 20,
        }}
        open={modal1Open}
        onOk={() => updateCity({ variables: { id:selectedItem.id,name: titleModify } })}
        onCancel={() => setModal1Open(false)}
      >
         <Form.Item label="Nom" initialValue={selectedItem?.name}>
          <Input placeholder="nom de ville" value={titleModify} onChange={onEditNameChange} />
        </Form.Item>
      
        
      </Modal>
      <List
      className="demo-loadmore-list"
      loading={loading}
      itemLayout="horizontal"
      dataSource={data.city}
      renderItem={(item) => (
        <List.Item
          actions={[ <a key="list-loadmore-more"  onClick={() => onEdit(item)  } ><EditFilled /></a>,<a key="list-loadmore-edit"><DeleteFilled onClick={() => deleteCity({ variables: { id:item.id } })} color="#eb2f96" style={{color:"#eb2f96" }} twoToneColor="#eb2f96"/></a>]}
        >
          <Skeleton avatar title={false} loading={loading} active>
            <List.Item.Meta
              title={item.name}
              description=" "
            />
          </Skeleton>
        </List.Item>
      )}
    />
    </div>
  );
}

export default App;
