import 'dart:convert';
import 'dart:io';
import 'dart:typed_data';

import 'package:http/http.dart' as http;
import 'package:camera/camera.dart';

import 'package:frontend/src/core/services/urldata.dart' as urldata;

final predictUrl = Uri.parse(urldata.predictUrl);
const headers = {'Content-Type': 'application/json'};

Future<String> makePrediction(XFile image) async {
  final Uint8List bytes = await image.readAsBytes();
  final String encoded = base64Encode(bytes);

  final String body = jsonEncode({
    'image': encoded,
  });

  final response = await http.post(predictUrl, headers: headers, body: body);

  print(response);

  if (response.statusCode == HttpStatus.ok) {
    final Map<String, dynamic> decoded = jsonDecode(response.body);
    return decoded['prediction'];
  } else {
    return 'Failed.';
  }
}