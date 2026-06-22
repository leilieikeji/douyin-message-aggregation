import api from './api';

export interface Message {
  id: string;
  account_id: string;
  sender_id: string;
  sender_name: string;
  content: string;
  status: 'unread' | 'read' | 'replied';
  created_at: string;
}

export const messageService = {
  async getMessages(skip = 0, limit = 20, accountId?: string, status?: string) {
    return api.get('/messages', {
      params: { skip, limit, account_id: accountId, status },
    });
  },

  async getMessage(messageId: string) {
    return api.get(`/messages/${messageId}`);
  },

  async searchMessages(keyword: string, skip = 0, limit = 20) {
    return api.post('/messages/search', { keyword, skip, limit });
  },

  async replyMessage(messageId: string, content: string) {
    return api.post(`/messages/${messageId}/reply`, { content });
  },
};
