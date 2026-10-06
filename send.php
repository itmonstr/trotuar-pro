<?php

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Метод не поддерживается'], JSON_UNESCAPED_UNICODE);
    exit;
}

$recipient = 'glebrazer2005@gmail.com';
$name = trim(isset($_POST['name']) ? (string)$_POST['name'] : '');
$phone = trim(isset($_POST['phone']) ? (string)$_POST['phone'] : '');
$task = trim(isset($_POST['task']) ? (string)$_POST['task'] : '');
$method = trim(isset($_POST['contact_method']) ? (string)$_POST['contact_method'] : '');
$telegram = trim(isset($_POST['telegram']) ? (string)$_POST['telegram'] : '');
$email = trim(isset($_POST['email']) ? (string)$_POST['email'] : '');
$trap = trim(isset($_POST['website']) ? (string)$_POST['website'] : '');

if ($trap !== '') {
    echo json_encode(['ok' => true], JSON_UNESCAPED_UNICODE);
    exit;
}

$phoneDigits = preg_replace('/\D+/', '', $phone);
$methods = array('phone' => 'Телефон', 'telegram' => 'Telegram', 'max' => 'MAX', 'email' => 'Почта');
$validName = mb_strlen($name, 'UTF-8') >= 2 && mb_strlen($name, 'UTF-8') <= 80;
$validPhone = preg_match('/^[78][0-9]{10}$/', $phoneDigits) === 1;
$validTask = mb_strlen($task, 'UTF-8') >= 5 && mb_strlen($task, 'UTF-8') <= 2000;
$validMethod = isset($methods[$method]);
$validTelegram = $method !== 'telegram' || preg_match('/^@[a-zA-Z0-9_]{5,32}$/', $telegram) === 1;
$validEmail = $method !== 'email' || (strlen($email) <= 254 && filter_var($email, FILTER_VALIDATE_EMAIL));

if (!$validName || !$validPhone || !$validTask || !$validMethod || !$validTelegram || !$validEmail) {
    http_response_code(422);
    echo json_encode(['ok' => false, 'error' => 'Проверьте имя, номер телефона и выбранный способ связи.'], JSON_UNESCAPED_UNICODE);
    exit;
}

$name = str_replace(array("\r", "\n"), ' ', $name);
$phone = '+7' . substr($phoneDigits, 1);
$subject = 'Новая заявка на сайте';
$body = "Имя: {$name}\nТелефон: {$phone}\nЧто нужно сделать: {$task}\nУдобный способ связи: {$methods[$method]}\n";
if ($method === 'telegram') {
    $body .= "Telegram: {$telegram}\n";
}
if ($method === 'email') {
    $body .= "Почта для связи: {$email}\n";
}
$body .= "Дата: " . date('d.m.Y H:i') . "\n";
$headers = "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nFrom: site@otalikl1.beget.tech\r\n";

$sent = mail($recipient, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers);
if (!$sent) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Почтовый сервер временно недоступен'], JSON_UNESCAPED_UNICODE);
    exit;
}

echo json_encode(['ok' => true], JSON_UNESCAPED_UNICODE);

