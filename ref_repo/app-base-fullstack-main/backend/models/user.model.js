const users = [ // bando de dados fake
  { id: 1, name: 'Lucas' },
  { id: 2, name: 'Ana' },
  { id: 3, name: 'João' },
];

// Função para obter todos os usuários
function getUsers(req, res) {
    res.send(users);
}


// Função para obter um usuário por ID
function getUserById(req, res) {

    console.log(req);
    const userId = parseInt(req.params.id);
    const user = users.find(u => u.id === userId);

    if (!user) {
        return res.status(404).send({ error: 'User not found' });
    }
    res.send(user);
}

function createUser(req, res) {

    console.log(req.body);
    const newUser = {
        id: users.length + 1,
        name: req.body.name
    };
    users.push(newUser);
    res.status(201).send(newUser);
}


module.exports = { getUsers, getUserById, createUser };