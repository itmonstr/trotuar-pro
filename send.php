<?php

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Метод не поддерживается'], JSON_UNESCAPED_UNICODE);
    exit;
}

// Замените этот адрес на почту, на которую должны приходить заявки.
$recipient = 'glebrazer2005@gmail.com';
$name = trim(isset($_POST['name']) ? (string)$_POST['name'] : '');
$phone = trim(isset($_POST['phone']) ? (string)$_POST['phone'] : '');
$task = trim(isset($_POST['task']) ? (string)$_POST['task'] : '');
$trap = trim(isset($_POST['website']) ? (string)$_POST['website'] : '');

if ($trap !== '') {
    echo json_encode(['ok' => true], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($name === '' || $phone === '' || $task === '') {
    http_response_code(422);
    echo json_encode(['ok' => false, 'error' => 'Форма ещё не настроена или заполнена не полностью'], JSON_UNESCAPED_UNICODE);
    exit;
}

$name = mb_substr($name, 0, 120);
$phone = mb_substr($phone, 0, 80);
$task = mb_substr($task, 0, 2000);
$subject = 'Новая заявка с сайта Тротуар_Про';
$body = "Новая заявка с сайта\n\nИмя: {$name}\nТелефон: {$phone}\nЗадача: {$task}\n\nДата: " . date('d.m.Y H:i') . "\n";
$hostValue = isset($_SERVER['HTTP_HOST']) ? (string)$_SERVER['HTTP_HOST'] : 'localhost';
$host = preg_replace('/[^a-z0-9.-]/i', '', $hostValue);
$host = $host ? $host : 'localhost';
$headers = "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nFrom: site@{$host}\r\n";

$sent = mail($recipient, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers);
if (!$sent) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Почтовый сервер временно недоступен'], JSON_UNESCAPED_UNICODE);
    exit;
}

echo json_encode(['ok' => true], JSON_UNESCAPED_UNICODE);
