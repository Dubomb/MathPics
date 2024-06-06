import 'package:flutter/material.dart';
import 'src/components/screens/homepage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Camera',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.lightBlue
        ),
        useMaterial3: true,
      ),
      home: HomePage(),
    );
  }
}