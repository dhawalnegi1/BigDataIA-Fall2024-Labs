JWT -> 
    JSON Web Token
    RFC 7519 standard 
    securely transmitting information between parties
    Infromation cna be verified and truested because it is digitally signed
    Compact and Self contained -> contain all necessary info about user
    Authetication vs Authorization

JWT Structure ->
    Header -> Contains metadata about type of token and hashing algo used
    Paylaod -> Contians claims about entity and additional data
    Signature -> Used for verifying authenticity of token

FatAPI setup ->
    poetry add fastapi uvicorn pyjwt
    Define your Secret Key

JWT Implementation
    Necessary Imports
    Implement Custon Password Hashing ->
        Use HMAC witpasswords h SHA-256 ro hash password using secret key
        Ensure RO never store password in plain texts
    Implement JWT TOken creation and decoding ->
        create_jwt_token
        decode_jwt_token
    Initialize FastAPI App and Security
    Create a palceholder DB for demo
    Implement Dependency to get current user ->
        Extracts the JWT token from the Authorization header.
        Decodes the token to get the username.
        Retrieves the user from the database.
        Raises an exception if authentication fails.
    Define API Endpoints ->
        User Login Endpoint
        Protected Endpoint

Run fastapi server via unicorn

Security Considerations and Best Practices ->
    Use environment variables to store secret keys
    HMAC with SHA-256 is acceptable for demo purposes, dedicated password hashing algorithms like bcrypt or Argon2 are used in production env
    

