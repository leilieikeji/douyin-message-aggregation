import { Layout, Menu, Space, Button, Dropdown, Card, Row, Col, Statistic, Table, Empty } from 'antd';
import {
  DesktopOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
  MailOutlined,
  LogoutOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
} from '@ant-design/icons';
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import React, { useState } from 'react';
import './App.css';

const { Header, Footer, Sider, Content } = Layout;

const Dashboard: React.FC = () => {
  return (
    <Row gutter={16} style={{ marginBottom: 24 }}>
      <Col xs={24} sm={12} lg={6}>
        <Card>
          <Statistic title="总消息数" value={0} />
        </Card>
      </Col>
      <Col xs={24} sm={12} lg={6}>
        <Card>
          <Statistic title="总账户数" value={0} />
        </Card>
      </Col>
      <Col xs={24} sm={12} lg={6}>
        <Card>
          <Statistic title="未读消息" value={0} />
        </Card>
      </Col>
      <Col xs={24} sm={12} lg={6}>
        <Card>
          <Statistic title="已回复" value={0} />
        </Card>
      </Col>
    </Row>
  );
};

const Messages: React.FC = () => {
  return (
    <Card title="消息列表">
      <Empty description="暂无消息" />
    </Card>
  );
};

const Accounts: React.FC = () => {
  return (
    <Card title="账户列表">
      <Empty description="暂无账户" />
    </Card>
  );
};

const AutoReply: React.FC = () => {
  return (
    <Card title="自动回复规则">
      <Empty description="暂无规则" />
    </Card>
  );
};

const AppContent: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  const location = useLocation();

  const getSelectedKey = () => {
    switch (location.pathname) {
      case '/messages':
        return '2';
      case '/accounts':
        return '3';
      case '/auto-reply':
        return '4';
      default:
        return '1';
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        trigger={null}
        collapsible
        collapsed={collapsed}
        width={200}
        style={{ background: '#001529' }}
      >
        <div style={{
          color: '#fff',
          padding: '16px',
          textAlign: 'center',
          fontSize: '16px',
          fontWeight: 'bold',
        }}>
          {collapsed ? 'DMA' : '抖音私信聚合'}
        </div>
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[getSelectedKey()]}
          items={[
            {
              key: '1',
              icon: <PieChartOutlined />,
              label: <Link to="/">仪表板</Link>,
            },
            {
              key: '2',
              icon: <MailOutlined />,
              label: <Link to="/messages">消息</Link>,
            },
            {
              key: '3',
              icon: <TeamOutlined />,
              label: <Link to="/accounts">账户</Link>,
            },
            {
              key: '4',
              icon: <DesktopOutlined />,
              label: <Link to="/auto-reply">自动回复</Link>,
            },
          ]}
        />
      </Sider>

      <Layout>
        <Header style={{ background: '#fff', padding: '0 16px', boxShadow: '0 2px 8px rgba(0,0,0,0.1)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Button
            type="text"
            icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
            onClick={() => setCollapsed(!collapsed)}
            style={{ fontSize: '16px', width: 64, height: 64 }}
          />
          <Space>
            <span>用户名</span>
            <Dropdown
              menu={{
                items: [
                  {
                    key: '1',
                    icon: <UserOutlined />,
                    label: '个人设置',
                  },
                  {
                    type: 'divider',
                  },
                  {
                    key: '2',
                    icon: <LogoutOutlined />,
                    label: '退出登录',
                  },
                ],
              }}
            >
              <Button type="primary" shape="circle" icon={<UserOutlined />} />
            </Dropdown>
          </Space>
        </Header>

        <Content style={{ margin: '24px' }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/messages" element={<Messages />} />
            <Route path="/accounts" element={<Accounts />} />
            <Route path="/auto-reply" element={<AutoReply />} />
          </Routes>
        </Content>

        <Footer style={{ textAlign: 'center' }}>
          抖音私信聚合系统 ©2024 Created by leilieikeji
        </Footer>
      </Layout>
    </Layout>
  );
};

const App: React.FC = () => {
  return (
    <Router>
      <AppContent />
    </Router>
  );
};

export default App;
