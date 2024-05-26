import { ObjectWithPermissions } from './object-with-permissions'

export enum IMAPSecurity {
  None = 1,
  SSL = 2,
  STARTTLS = 3,
  SSL_NO_HOST_CHECK = 4,
  STARTTLS_NO_HOST_CHECK = 5, 
  SSL_ALLOW_INVALID_CERT = 6,
  STARTTLS_ALLOW_INVALID_CERT = 7, 
}

export interface MailAccount extends ObjectWithPermissions {
  name: string

  imap_server: string

  imap_port: number

  imap_security: IMAPSecurity

  username: string

  password: string

  character_set?: string

  is_token: boolean
}
