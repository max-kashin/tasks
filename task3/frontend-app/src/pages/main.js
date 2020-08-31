import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Row, Col, Card, Tag, Button } from 'antd';
import { Link } from 'react-router-dom';

const Main = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    async function fetch() {
      const { data: events } = await axios.get('http://localhost:8000/events');
      console.log(events)
      setEvents(events);
    }
    fetch();
  }, []);

  return events.length ? (
    <div>
      <Row align="middle">
        <Col span={7} offset={8}>
          <h1>World saving history</h1>
        </Col>
        <Col span={1}>
          <Link to="/create">
            <Button>Add</Button>
          </Link>
        </Col>
      </Row>
      <Row>
        <Col span={8} offset={8}>
          {events.map(event => (
            <Card
              title={new Date(event.date).toLocaleDateString(undefined, {
                year: 'numeric',
                month: 'numeric',
                day: 'numeric',
              })}
              key={event.id}
              style={{ marginBottom: 20 }}
            >
              <div>{event.description}</div>
              {event.persons && event.persons.length && (
                <>
                  <div>
                    The people I'm thankful to:
                  </div>
                  <div>
                    {event.persons.map(person => (
                      <Tag key={person.id}>
                        {person.name}
                      </Tag>
                    ))}
                  </div>
                </>
              )}
            </Card>
          ))}
        </Col>
      </Row>
    </div>
  ) : (
    <div>No events here</div>
  );
}

export default Main;
