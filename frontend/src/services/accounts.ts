import api from './api';

export interface Account {
  id: string;
  name: string;
  avatar: string;
  status: 'active' | 'inactive';
  messages_count: number;
  created_at: string;
}

export const accountService = {
  async getAccounts(skip = 0, limit = 20) {
    return api.get('/accounts', {
      params: { skip, limit },
    });
  },

  async getAccount(accountId: string) {
    return api.get(`/accounts/${accountId}`);
  },

  async createAccount(data: Partial<Account>) {
    return api.post('/accounts', data);
  },

  async updateAccount(accountId: string, data: Partial<Account>) {
    return api.put(`/accounts/${accountId}`, data);
  },

  async deleteAccount(accountId: string) {
    return api.delete(`/accounts/${accountId}`);
  },
};
