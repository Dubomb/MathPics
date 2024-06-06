import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "MathPics",
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blueGrey),
        useMaterial3: true,
      ),
      home: Scaffold(
        body: Column(
          children: [
            const Center(
              child: Text('Hello World!'),
            ),
            ElevatedButton(onPressed: () {}, child: const Text('Press me!')),
          ],
        ),
      ),
    );
  }
}
