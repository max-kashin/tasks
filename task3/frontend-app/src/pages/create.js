import React, { useState } from 'react';

import {
  Row,
  Col,
  Button,
  Form,
  Input,
  DatePicker,
  AutoComplete,
  Tag,
} from 'antd';
import { ArrowLeftOutlined } from '@ant-design/icons';
import { Link } from 'react-router-dom';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 8 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 8 },
};

const { TextArea } = Input;

const mockVal = (str, repeat = 1) => {
  return {
    value: str.repeat(repeat),
  };
};

const Create = () => {
  const [value, setValue] = useState('');
  const [options, setOptions] = useState([]);
  const [persons, setPersons] = useState([]);
  const onSearch = (searchText) => {
    setOptions(
      !searchText ? [] : [mockVal(searchText), mockVal(searchText, 2), mockVal(searchText, 3)],
    );
  };
  const onSelect = (data) => {
    setPersons([...persons, data]);
  };

  const onChange = (data) => {
    setValue(data);
  };

  const onRemovePerson = (id) => {
    setPersons([]);
  };

  return (
    <div>
      <Row>
        <Col span={8} offset={8}>
          <h1 style={{margin: 0}}>
            Add new record about world saving
          </h1>
        </Col>
      </Row>
      <Row>
        <Col span={8} offset={8}>
          <Link to="/">
            <Button
              type="link"
              icon={<ArrowLeftOutlined />}
              style={{padding: 0, marginBottom: 20}}
            >
              Back to main page
            </Button>
          </Link>
        </Col>
      </Row>
      <Form
        {...layout}
        name="basic"
        initialValues={{ remember: true }}
      >
        <Form.Item
          label="Description"
          rules={[{
            required: true,
            message: 'Please provide correct description'
          }]}
        >
          <TextArea rows={4} />
        </Form.Item>

        <Form.Item
          label="When you saved the world"
          rules={[{
            required: true,
            message: 'Please input correct date'
          }]}
        >
          <DatePicker />
        </Form.Item>

        <Form.Item
          label="People you are thankful to"
          rules={[{
            required: true,
            message: 'Please input correct date'
          }]}
        >
          <AutoComplete
            options={options}
            style={{ width: 200 }}
            onSelect={onSelect}
            onSearch={onSearch}
            placeholder="input here"
          />
          <div>
            {persons.map(person => (
              <Tag closable onClose={onRemovePerson}>
                {person}
              </Tag>
            ))}
          </div>
        </Form.Item>

        <Form.Item {...tailLayout}>
          <Button type="primary" htmlType="submit">
            Save
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}

export default Create;
